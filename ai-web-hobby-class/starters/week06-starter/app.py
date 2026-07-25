"""
AI웹반 6주차 — Python prompt + AI 퀴즈 생성
https://app.notion.com/p/api-key-399b05b3ee658079a0edd3dd50cab208

[🟢] 이번 주: DEFAULT_SUBJECT 바꾸기 → 퀴즈 생성 버튼 → AI 퀴즈 확인!
[🟡] build_quiz_prompt() 에 「쉬운 난이도」 추가
[🔴] 생성 결과를 4주차 OX 형식으로 파싱 (선택)
[7주~] 챗봇 + 퀴즈를 한 앱(탭)으로 통합
"""
import os

from flask import Flask, jsonify, render_template, request
from openai import OpenAI

app = Flask(__name__)

STUDENT_NAME = "홍길동"

# OpenRouter — OpenAI SDK 호환 API (https://openrouter.ai)
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
AI_MODEL = "openrouter/free"  # 무료 모델 — openrouter.ai/collections/free-models


# ===== [🟢] 기본 과목 — 바꿔보세요 =====
DEFAULT_SUBJECT = "영어 단어"


# ===== [🟡] call_ai() — 5주차와 동일 (Python이 AI를 부름) =====
def call_ai(prompt: str) -> str:
    """API 키는 Replit Secrets (OPENROUTER_API_KEY) — JS에는 키 없음!"""
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        return "⚠️ Replit Secrets에 OPENROUTER_API_KEY 를 설정해 주세요. (교사에게 문의)"

    client = OpenAI(base_url=OPENROUTER_BASE_URL, api_key=api_key)
    response = client.chat.completions.create(
        model=AI_MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content or ""


# ===== [🟢] build_quiz_prompt() — Python이 prompt를 설계합니다 =====
def build_quiz_prompt(subject: str) -> str:
    """과목(subject)만 받아서 AI에게 줄 문장을 만듭니다."""
    # [🟡] 도전: 「쉬운 난이도」 같은 조건을 여기에 추가해 보세요
    return f"중학생용 {subject} 퀴즈 3문제를 OX 형식으로 만들어줘. 각 문제 뒤에 (정답: O 또는 X)를 적어줘."


@app.route("/")
def home():
    """AI 퀴즈 생성 페이지 — 기본 과목은 Python DEFAULT_SUBJECT."""
    return render_template(
        "index.html",
        name=STUDENT_NAME,
        default_subject=DEFAULT_SUBJECT,
    )


@app.route("/api/generate-quiz")
def api_generate_quiz():
    """브라우저 fetch → Python build_quiz_prompt() → call_ai() → JSON."""
    subject = (request.args.get("subject") or "").strip()
    if not subject:
        subject = DEFAULT_SUBJECT

    prompt = build_quiz_prompt(subject)
    quiz = call_ai(prompt)
    return jsonify({"quiz": quiz, "subject": subject, "prompt": prompt})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)
