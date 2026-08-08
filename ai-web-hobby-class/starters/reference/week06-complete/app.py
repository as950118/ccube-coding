"""
AI웹반 6주차 — 완성 예시 (교사 시연용)
https://app.notion.com/p/api-key-399b05b3ee658079a0edd3dd50cab208
쉬운 난이도 prompt + 로딩 표시 포함
"""
import os

from flask import Flask, jsonify, render_template, request
from openai import OpenAI

app = Flask(__name__)

STUDENT_NAME = "김서연"
DEFAULT_SUBJECT = "과학"

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
AI_MODEL = "openrouter/free"


def call_ai(prompt: str) -> str:
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        return "⚠️ Replit Secrets에 OPENROUTER_API_KEY 를 설정해 주세요."

    client = OpenAI(base_url=OPENROUTER_BASE_URL, api_key=api_key)
    response = client.chat.completions.create(
        model=AI_MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content or ""


def build_quiz_prompt(subject: str) -> str:
    return (
        f"중학생용 {subject} 퀴즈 3문제를 OX 형식으로 만들어줘. "
        f"쉬운 난이도로, 각 문제 뒤에 (정답: O 또는 X)를 적어줘."
    )


@app.route("/")
def home():
    return render_template(
        "index.html",
        name=STUDENT_NAME,
        default_subject=DEFAULT_SUBJECT,
    )


@app.route("/api/generate-quiz")
def api_generate_quiz():
    subject = (request.args.get("subject") or "").strip() or DEFAULT_SUBJECT
    prompt = build_quiz_prompt(subject)
    quiz = call_ai(prompt)
    return jsonify({"quiz": quiz, "subject": subject, "prompt": prompt})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)
