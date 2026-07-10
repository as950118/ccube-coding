"""
AI웹반 4주차 — 완성 예시 (교사 시연용)
"""
import os

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

STUDENT_NAME = "김서연"

QUESTIONS = [
    {"text": "Python은 프로그래밍 언어이다.", "answer": "O"},
    {"text": "HTML은 데이터베이스이다.", "answer": "X"},
    {"text": "Flask는 Python 웹 프레임워크이다.", "answer": "O"},
    {"text": "CSS는 웹 페이지 꾸미기에 쓰인다.", "answer": "O"},
]


def check_answer(q_index: int, user_answer: str) -> bool:
    if q_index < 0 or q_index >= len(QUESTIONS):
        return False
    return user_answer.upper() == QUESTIONS[q_index]["answer"]


@app.route("/")
def home():
    return render_template("index.html", name=STUDENT_NAME, questions=QUESTIONS)


@app.route("/api/check")
def api_check():
    q_index = int(request.args.get("q", 0))
    user_answer = request.args.get("answer", "")

    correct = check_answer(q_index, user_answer)
    return jsonify({
        "correct": correct,
        "message": "맞아요! 🎉" if correct else "틀려요 😅",
    })


@app.route("/api/score")
def api_score():
    raw = request.args.get("answers", "")
    answers = [a.strip().upper() for a in raw.split(",") if a.strip()]
    score = sum(
        1 for i, ans in enumerate(answers)
        if i < len(QUESTIONS) and ans == QUESTIONS[i]["answer"]
    )
    return jsonify({"score": score, "total": len(QUESTIONS)})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)
