"""
AI웹반 5주차 — 완성 예시 (교사 시연용)
"""
import os

from flask import Flask, jsonify, render_template, request
from openai import OpenAI

app = Flask(__name__)

STUDENT_NAME = "김서연"
DEFAULT_QUESTION = "중학생에게 공부 팁 한 가지만 알려줘"

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
AI_MODEL = "google/gemma-4-31b-it:free"


def call_ai(question: str) -> str:
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        return "⚠️ Replit Secrets에 OPENROUTER_API_KEY 를 설정해 주세요."

    client = OpenAI(base_url=OPENROUTER_BASE_URL, api_key=api_key)
    response = client.chat.completions.create(
        model=AI_MODEL,
        messages=[{"role": "user", "content": question}],
    )
    return response.choices[0].message.content or ""


@app.route("/")
def home():
    return render_template(
        "index.html",
        name=STUDENT_NAME,
        default_question=DEFAULT_QUESTION,
    )


@app.route("/api/chat", methods=["POST"])
def api_chat():
    data = request.get_json(silent=True) or {}
    question = (data.get("question") or "").strip()
    if not question:
        question = DEFAULT_QUESTION

    reply = call_ai(question)
    return jsonify({"reply": reply, "question": question})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
