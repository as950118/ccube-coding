"""
AI웹반 3주차 — Python 함수 + fetch: 브라우저가 Python에게 계산 부탁

[🟢] 이번 주: 숫자 2개 입력 → 더하기 버튼 → 결과 확인!
[🟡] def subtract + /api/sub 추가
[🔴] 0·빈 값 입력 시 「숫자를 입력하세요」
[5주~] Python 이 AI API 를 호출합니다.
"""
import os

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# ===== 2주차 이어가기 — 자기소개 (읽기) =====
STUDENT_NAME = "홍길동"


# ===== [🟢] Python 함수 — add(a, b) =====
def add(a: int, b: int) -> int:
    """두 숫자를 더합니다."""
    return a + b


# ===== [🟡] 도전: 빼기 함수 =====
def subtract(a: int, b: int) -> int:
    return a - b


@app.route("/")
def home():
    """자기소개 페이지 + 계산기 UI."""
    return render_template("index.html", name=STUDENT_NAME)


@app.route("/api/add")
def api_add():
    """브라우저 fetch → Python add() → JSON."""
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))

    # ===== [🔴] 도전: a==0 and b==0 이면 에러 JSON =====
    # if a == 0 and b == 0:
    #     return jsonify({"error": "숫자를 입력하세요"}), 400

    return jsonify({"sum": add(a, b)})


# ===== [🟡] 도전: 빼기 API =====
@app.route("/api/sub")
def api_sub():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return jsonify({"diff": subtract(a, b)})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)
