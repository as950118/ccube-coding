"""
AI웹반 7주차 — 완성 예시 (교사 시연용)
챗봇·퀴즈·OX 3탭 + TUTOR_PROMPT
"""
import os

from flask import Flask, jsonify, render_template, request
from openai import OpenAI

app = Flask(__name__)

APP_TITLE = "서연의 AI 학습 도우미"
STUDENT_NAME = "김서연"

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
AI_MODEL = "google/gemma-4-31b-it:free"

DEFAULT_QUESTION = "오늘 공부 계획을 세워줘"
DEFAULT_SUBJECT = "과학"
TUTOR_PROMPT = "너는 중학생을 도와주는 친절한 튜터야. 쉽고 짧게, 응원하며 설명해 줘."

QUESTIONS = [
    {"text": "Python은 프로그래밍 언어이다.", "answer": "O"},
    {"text": "HTML은 데이터베이스이다.", "answer": "X"},
    {"text": "Flask는 Python 웹 프레임워크이다.", "answer": "O"},
    {"text": "CSS는 웹 페이지 꾸미기에 쓰인다.", "answer": "O"},
]


def call_ai(question: str) -> str:
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        return "⚠️ Replit Secrets에 OPENROUTER_API_KEY 를 설정해 주세요."

    client = OpenAI(base_url=OPENROUTER_BASE_URL, api_key=api_key)
    response = client.chat.completions.create(
        model=AI_MODEL,
        messages=[
            {"role": "system", "content": TUTOR_PROMPT},
            {"role": "user", "content": question},
        ],
    )
    return response.choices[0].message.content or ""


def build_quiz_prompt(subject: str) -> str:
    return (
        f"중학생용 {subject} 퀴즈 3문제를 OX 형식으로 만들어줘. "
        f"쉬운 난이도로, 각 문제 뒤에 (정답: O 또는 X)를 적어줘."
    )


def check_answer(q_index: int, user_answer: str) -> bool:
    if q_index < 0 or q_index >= len(QUESTIONS):
        return False
    return user_answer.upper() == QUESTIONS[q_index]["answer"]


@app.route("/")
def home():
    return render_template(
        "index.html",
        app_title=APP_TITLE,
        name=STUDENT_NAME,
        default_question=DEFAULT_QUESTION,
        default_subject=DEFAULT_SUBJECT,
        questions=QUESTIONS,
    )


@app.route("/api/chat", methods=["POST"])
def api_chat():
    data = request.get_json(silent=True) or {}
    question = (data.get("question") or "").strip() or DEFAULT_QUESTION
    return jsonify({"reply": call_ai(question), "question": question})


@app.route("/api/generate-quiz")
def api_generate_quiz():
    subject = (request.args.get("subject") or "").strip() or DEFAULT_SUBJECT
    quiz = call_ai(build_quiz_prompt(subject))
    return jsonify({"quiz": quiz, "subject": subject})


@app.route("/api/check")
def api_check():
    q_index = int(request.args.get("q", 0))
    user_answer = request.args.get("answer", "")
    correct = check_answer(q_index, user_answer)
    return jsonify({
        "correct": correct,
        "message": "맞아요! 🎉" if correct else "틀려요 😅",
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)
