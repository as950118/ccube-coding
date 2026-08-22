"""
AI웹반 11주차 — 통합: Python + 텍스트 AI + 이미지 AI + 웹
https://app.notion.com/p/api-key-399b05b3ee658079a0edd3dd50cab208

[🟢] 이번 주: APP_TITLE · STUDENT_NAME 바꾸기 → 메뉴 4개(챗봇·퀴즈·OX·이미지 AI) 확인!
[🟡] TUTOR_PROMPT — 친절한 튜터 system prompt / 다크모드는 style.css
[🔴] Replit Deploy → URL 받기 (발표 준비)

5~8주차: 텍스트 AI (/api/chat, /api/generate-quiz)
4주차: OX 채점 (/api/check)
9~10주차: 이미지 AI (Teachable Machine, 브라우저 JS — Python은 MODEL_URL만 전달)
→ 오늘은 넷을 한 앱, 한 화면(탭 메뉴)으로 합칩니다!
"""
import os

from flask import Flask, jsonify, render_template, request
from openai import OpenAI

app = Flask(__name__)

# ===== [🟢] 사이트 제목 · 이름 — 바꿔보세요 =====
APP_TITLE = "나만의 AI 학습 도우미"
STUDENT_NAME = "홍길동"

# OpenRouter — OpenAI SDK 호환 API (https://openrouter.ai)
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
AI_MODEL = "openrouter/free"

DEFAULT_QUESTION = "오늘 공부 계획을 세워줘"
DEFAULT_SUBJECT = "과학"

# ===== [🟡] 튜터 톤 — call_ai 에 system 으로 넣습니다 =====
TUTOR_PROMPT = "너는 중학생을 도와주는 친절한 튜터야. 쉽고 짧게, 응원하며 설명해 줘."

# ===== 4주차 OX =====
QUESTIONS = [
    {"text": "Python은 프로그래밍 언어이다.", "answer": "O"},
    {"text": "HTML은 데이터베이스이다.", "answer": "X"},
    {"text": "Flask는 Python 웹 프레임워크이다.", "answer": "O"},
    {"text": "CSS는 웹 페이지 꾸미기에 쓰인다.", "answer": "O"},
]

# ===== 9~10주차 Teachable Machine 모델 URL — 끝에 / 포함! =====
# 예: https://teachablemachine.withgoogle.com/models/XXXXXXXX/
MODEL_URL = "https://teachablemachine.withgoogle.com/models/GFzCz0vn0/"


def call_ai(question: str) -> str:
    """API 키는 Replit Secrets (OPENROUTER_API_KEY) — JS에는 키 없음!"""
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        return "⚠️ Replit Secrets에 OPENROUTER_API_KEY 를 설정해 주세요. (교사에게 문의)"

    client = OpenAI(base_url=OPENROUTER_BASE_URL, api_key=api_key)
    response = client.chat.completions.create(
        model=AI_MODEL,
        messages=[
            # [🟡] system prompt — TUTOR_PROMPT 사용
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
    """한 페이지에 챗봇·퀴즈·OX·이미지 AI 메뉴(탭) 4개."""
    return render_template(
        "index.html",
        app_title=APP_TITLE,
        name=STUDENT_NAME,
        default_question=DEFAULT_QUESTION,
        default_subject=DEFAULT_SUBJECT,
        questions=QUESTIONS,
        model_url=MODEL_URL,
    )


@app.route("/api/chat", methods=["POST"])
def api_chat():
    """5주차 — AI 챗."""
    data = request.get_json(silent=True) or {}
    question = (data.get("question") or "").strip() or DEFAULT_QUESTION
    return jsonify({"reply": call_ai(question), "question": question})


@app.route("/api/generate-quiz")
def api_generate_quiz():
    """6주차 — AI 퀴즈 생성."""
    subject = (request.args.get("subject") or "").strip() or DEFAULT_SUBJECT
    quiz = call_ai(build_quiz_prompt(subject))
    return jsonify({"quiz": quiz, "subject": subject})


@app.route("/api/check")
def api_check():
    """4주차 — OX 채점."""
    q_index = int(request.args.get("q", 0))
    user_answer = request.args.get("answer", "")
    correct = check_answer(q_index, user_answer)
    return jsonify({
        "correct": correct,
        "message": "맞아요! 🎉" if correct else "틀려요 😅",
    })


# 이미지 AI(TM)는 브라우저 JS가 직접 처리 — Python은 MODEL_URL만 전달, 별도 API 없음


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)
