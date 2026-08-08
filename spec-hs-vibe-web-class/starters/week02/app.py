from flask import Flask, request, jsonify, render_template
import sqlite3
from pathlib import Path


app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / "chat.db"


# =====================================
# 선생님 공지
# 수업 전에 내용을 변경하세요.
# =====================================
NOTICE = """
오늘의 실습

1. 학생 ID는 선생님이 지정한 ID를 사용합니다.
2. POST 요청으로 채팅을 전송합니다.
3. GET 요청으로 선생님 공지를 가져옵니다.
4. 다른 학생에게 불쾌감을 줄 수 있는 내용은 작성하지 않습니다.
""".strip()


# =====================================
# 데이터베이스 연결
# =====================================
def get_db():
    conn = sqlite3.connect(
        DATABASE,
        timeout=10
    )

    conn.row_factory = sqlite3.Row

    # DB가 잠겨 있으면 최대 10초 대기
    conn.execute("PRAGMA busy_timeout = 10000")

    return conn


# =====================================
# 테이블 생성
# =====================================
def create_table():
    conn = get_db()

    try:
        # 여러 요청이 동시에 들어올 때 충돌 감소
        conn.execute("PRAGMA journal_mode = WAL")

        conn.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT NOT NULL,
                message TEXT NOT NULL,
                created_at TEXT DEFAULT (
                    datetime('now', 'localtime')
                )
            )
        """)

        conn.commit()

    finally:
        conn.close()


# =====================================
# 채팅 데이터를 리스트로 변환
# =====================================
def rows_to_messages(rows):
    messages = []

    for row in rows:
        messages.append({
            "id": row["id"],
            "student_id": row["student_id"],
            "message": row["message"],
            "created_at": row["created_at"]
        })

    return messages


# =====================================
# 최근 채팅 조회
# =====================================
def select_recent_messages(conn, limit=50):
    rows = conn.execute("""
        SELECT
            id,
            student_id,
            message,
            created_at
        FROM messages
        ORDER BY id DESC
        LIMIT ?
    """, (limit,)).fetchall()

    # 오래된 메시지부터 나오도록 순서 변경
    rows = list(reversed(rows))

    return rows_to_messages(rows)


# =====================================
# 웹 채팅방
# GET /
# =====================================
@app.route("/")
def index():
    return render_template(
        "index.html",
        notice=NOTICE
    )


# =====================================
# 선생님 공지 조회
# GET /api/notice
# =====================================
@app.route("/api/notice", methods=["GET"])
def get_notice():
    return jsonify({
        "success": True,
        "notice": NOTICE
    }), 200


# =====================================
# 최근 채팅 조회
# GET /api/messages
# =====================================
@app.route("/api/messages", methods=["GET"])
def get_messages():
    conn = get_db()

    try:
        messages = select_recent_messages(
            conn,
            limit=50
        )

        return jsonify({
            "success": True,
            "count": len(messages),
            "messages": messages
        }), 200

    finally:
        conn.close()


# =====================================
# 새로운 채팅 전송
# POST /api/messages
# =====================================
@app.route("/api/messages", methods=["POST"])
def create_message():
    data = request.get_json(silent=True)

    # JSON 데이터 확인
    if data is None:
        return jsonify({
            "success": False,
            "message": "JSON 형식으로 데이터를 전송해야 합니다."
        }), 400

    # 데이터 가져오기
    student_id = str(
        data.get("student_id", "")
    ).strip()

    message = str(
        data.get("message", "")
    ).strip()

    # 학생 ID 검사
    if not student_id:
        return jsonify({
            "success": False,
            "message": "학생 ID를 입력해야 합니다."
        }), 400

    if len(student_id) > 20:
        return jsonify({
            "success": False,
            "message": "학생 ID는 20글자 이하로 작성하세요."
        }), 400

    # 메시지 검사
    if not message:
        return jsonify({
            "success": False,
            "message": "메시지를 입력해야 합니다."
        }), 400

    if len(message) > 100:
        return jsonify({
            "success": False,
            "message": "메시지는 100글자 이하로 작성하세요."
        }), 400

    conn = None

    try:
        conn = get_db()

        # 채팅 저장
        cursor = conn.execute("""
            INSERT INTO messages (
                student_id,
                message
            )
            VALUES (?, ?)
        """, (
            student_id,
            message
        ))

        conn.commit()

        message_id = cursor.lastrowid

        # 저장 후 최근 채팅 반환
        messages = select_recent_messages(
            conn,
            limit=50
        )

        return jsonify({
            "success": True,
            "message": "채팅이 전송되었습니다.",
            "message_id": message_id,
            "messages": messages
        }), 200

    except sqlite3.OperationalError as error:
        if conn is not None:
            conn.rollback()

        print("데이터베이스 오류:", error)

        return jsonify({
            "success": False,
            "message": "데이터베이스가 사용 중입니다."
        }), 503

    except Exception as error:
        if conn is not None:
            conn.rollback()

        print("서버 오류:", error)

        return jsonify({
            "success": False,
            "message": "서버에서 오류가 발생했습니다."
        }), 500

    finally:
        if conn is not None:
            conn.close()


# =====================================
# 전체 채팅 삭제
# 선생님 관리용
# DELETE /api/messages
# =====================================
@app.route("/api/messages", methods=["DELETE"])
def delete_all_messages():
    conn = None

    try:
        conn = get_db()

        conn.execute("DELETE FROM messages")

        # 자동 증가 번호 초기화
        conn.execute("""
            DELETE FROM sqlite_sequence
            WHERE name = 'messages'
        """)

        conn.commit()

        return jsonify({
            "success": True,
            "message": "모든 채팅이 삭제되었습니다."
        }), 200

    except sqlite3.OperationalError as error:
        if conn is not None:
            conn.rollback()

        print("데이터베이스 오류:", error)

        return jsonify({
            "success": False,
            "message": "채팅을 삭제하지 못했습니다."
        }), 503

    finally:
        if conn is not None:
            conn.close()


# =====================================
# 서버 실행
# =====================================
if __name__ == "__main__":
    create_table()

    app.run(
        host="0.0.0.0",
        port=5001,
        debug=False,
        threaded=True
    )