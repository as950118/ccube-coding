"""
AI웹반 8주차 — 완성 예시 (교사 시연용)
말풍선 UI + history + /api/clear
"""
import os

from flask import Flask, jsonify, render_template, request
from openai import OpenAI

app = Flask(__name__)

STUDENT_NAME = "김서연"
APP_TITLE = "서연의 말풍선 채팅"

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
AI_MODEL = "google/gemma-4-31b-it:free"
TUTOR_PROMPT = "너는 중학생을 도와주는 친절한 튜터야. 쉽고 짧게, 응원하며 설명해 줘."

messages: list[dict] = []


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


@app.route("/")
def home():
    return render_template("index.html", name=STUDENT_NAME, app_title=APP_TITLE)


@app.route("/api/chat", methods=["POST"])
def api_chat():
    data = request.get_json(silent=True) or {}
    question = (data.get("question") or "").strip()
    if not question:
        return jsonify({"error": "질문을 입력해 주세요!"}), 400

    reply = call_ai(question)
    messages.append({"role": "user", "text": question})
    messages.append({"role": "ai", "text": reply})
    return jsonify({"reply": reply, "history": messages})


@app.route("/api/clear", methods=["POST"])
def api_clear():
    messages.clear()
    return jsonify({"ok": True, "history": messages})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)
