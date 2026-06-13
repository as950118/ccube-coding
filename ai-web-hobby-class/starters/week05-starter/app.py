"""
AI웹반 5주차 — Python + AI: Flask가 AI에게 질문하기 ★

[🟢] 이번 주: DEFAULT_QUESTION 바꾸기 → AI 답 확인!
[🟡] 입력창에서 질문 보내기 (POST JSON)
[🔴] 「생각 중…」 로딩 표시 (JS)
[6주~] build_quiz_prompt() 로 prompt 설계
"""
import os

from flask import Flask, jsonify, render_template, request
from openai import OpenAI

app = Flask(__name__)

STUDENT_NAME = "홍길동"

# OpenRouter — OpenAI SDK 호환 API (https://openrouter.ai)
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
AI_MODEL = "google/gemma-4-31b-it:free"  # 무료 모델 — openrouter.ai/collections/free-models


# ===== [🟢] 기본 질문 — 바꿔보세요 =====
DEFAULT_QUESTION = "중학생에게 공부 팁 한 가지만 알려줘"


# ===== [🟡] call_ai() — Python이 AI API를 호출합니다 =====
def call_ai(question: str) -> str:
    """API 키는 Replit Secrets (OPENROUTER_API_KEY) — JS에는 키 없음!"""
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        return "⚠️ Replit Secrets에 OPENROUTER_API_KEY 를 설정해 주세요. (교사에게 문의)"

    client = OpenAI(base_url=OPENROUTER_BASE_URL, api_key=api_key)
    response = client.chat.completions.create(
        model=AI_MODEL,
        messages=[{"role": "user", "content": question}],
    )
    return response.choices[0].message.content or ""


@app.route("/")
def home():
    """AI 챗봇 페이지 — 기본 질문은 Python DEFAULT_QUESTION."""
    return render_template(
        "index.html",
        name=STUDENT_NAME,
        default_question=DEFAULT_QUESTION,
    )


@app.route("/api/chat", methods=["POST"])
def api_chat():
    """브라우저 fetch → Python call_ai() → OpenRouter → JSON."""
    data = request.get_json(silent=True) or {}
    question = (data.get("question") or "").strip()
    if not question:
        question = DEFAULT_QUESTION

    reply = call_ai(question)
    return jsonify({"reply": reply, "question": question})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
