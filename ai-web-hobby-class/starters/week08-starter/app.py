"""
AI웹반 8주차 — Python 대화 기록 + 채팅 UI (말풍선)
https://app.notion.com/p/api-key-399b05b3ee658079a0edd3dd50cab208

[🟢] 이번 주: 말풍선 색 바꾸기 → 질문·답 2턴 이상 쌓이기!
[🟡] /api/chat 가 history(Python list) 반환
[🔴] /api/clear — 대화 기록 비우기
[9주~] Teachable Machine 이미지 AI
"""
import os

from flask import Flask, jsonify, render_template, request
from openai import OpenAI

app = Flask(__name__)

STUDENT_NAME = "홍길동"
APP_TITLE = "말풍선 AI 채팅"

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
AI_MODEL = "openrouter/free"

TUTOR_PROMPT = "너는 중학생을 도와주는 친절한 튜터야. 쉽고 짧게 설명해 줘."

# ===== [🟡] Python이 대화 기록을 보관합니다 =====
messages: list[dict] = []


def call_ai(question: str) -> str:
    """API 키는 Replit Secrets (OPENROUTER_API_KEY) — JS에는 키 없음!"""
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        return "⚠️ Replit Secrets에 OPENROUTER_API_KEY 를 설정해 주세요. (교사에게 문의)"

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
    return render_template(
        "index.html",
        name=STUDENT_NAME,
        app_title=APP_TITLE,
    )


@app.route("/api/chat", methods=["POST"])
def api_chat():
    """질문 → AI 답 → Python messages 에 쌓고 history 반환."""
    data = request.get_json(silent=True) or {}
    question = (data.get("question") or "").strip()
    if not question:
        return jsonify({"error": "질문을 입력해 주세요!"}), 400

    reply = call_ai(question)

    # [🟡] Python list 에 대화 기록
    messages.append({"role": "user", "text": question})
    messages.append({"role": "ai", "text": reply})

    return jsonify({"reply": reply, "history": messages})


# ===== [🔴] 도전: 대화 기록 비우기 =====
@app.route("/api/clear", methods=["POST"])
def api_clear():
    messages.clear()
    return jsonify({"ok": True, "history": messages})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)
