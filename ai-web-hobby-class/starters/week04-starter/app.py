"""
AI웹반 4주차 — Python OX 퀴즈: 정답은 주방(Python)에서

[🟢] 이번 주: O/X 버튼 → fetch /api/check → Python이 정답 판정!
[🟡] QUESTIONS 에 문제 4번째 추가
[🔴] 3문제 끝 → /api/score 로 총점
[5주~] Python 이 AI API 를 호출합니다.
"""
import os

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

STUDENT_NAME = "홍길동"


# ===== [🟢] Python dict — 문제·정답은 여기서 관리 =====
QUESTIONS = [
    {"text": "Python은 프로그래밍 언어이다.", "answer": "O"},
    {"text": "HTML은 데이터베이스이다.", "answer": "X"},
    {"text": "Flask는 Python 웹 프레임워크이다.", "answer": "O"},
]


def check_answer(q_index: int, user_answer: str) -> bool:
    """Python이 O/X 정답을 판정합니다."""
    if q_index < 0 or q_index >= len(QUESTIONS):
        return False
    return user_answer.upper() == QUESTIONS[q_index]["answer"]


@app.route("/")
def home():
    """OX 퀴즈 페이지 — 문제 목록은 Python QUESTIONS 에서 전달."""
    return render_template("index.html", name=STUDENT_NAME, questions=QUESTIONS)


@app.route("/api/check")
def api_check():
    """브라우저 fetch → Python check_answer() → 맞/틀 JSON."""
    q_index = int(request.args.get("q", 0))
    user_answer = request.args.get("answer", "")

    correct = check_answer(q_index, user_answer)
    return jsonify({
        "correct": correct,
        "message": "맞아요! 🎉" if correct else "틀려요 😅",
    })


# ===== [🔴] 도전: 모든 문제 답 제출 후 총점 =====
# @app.route("/api/score")
# def api_score():
#     """answers=O,X,O 형식으로 받아 Python이 맞은 개수를 셉니다."""
#     raw = request.args.get("answers", "")
#     answers = [a.strip().upper() for a in raw.split(",") if a.strip()]
#     score = sum(
#         1 for i, ans in enumerate(answers)
#         if i < len(QUESTIONS) and ans == QUESTIONS[i]["answer"]
#     )
#     return jsonify({"score": score, "total": len(QUESTIONS)})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)
