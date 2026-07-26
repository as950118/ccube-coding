"""
AI웹반 7주차 — Flask 라우트 통합: AI 학습 도우미 한 앱
https://app.notion.com/p/api-key-399b05b3ee658079a0edd3dd50cab208

[🟢] 이번 주: APP_TITLE · 탭 이름 바꾸기 → 챗봇/퀴즈 탭 클릭!
[🟡] TUTOR_PROMPT — 친절한 튜터 system prompt
[🔴] OX 퀴즈를 세 번째 탭으로 (4주차 /api/check)
[8주~] messages[] + 말풍선 UI
"""
import os

from flask import Flask, jsonify, render_template, request
from openai import OpenAI

app = Flask(__name__)

# ===== [🟢] 사이트 제목 — 바꿔보세요 =====
APP_TITLE = "SPA AI 웹사이트"
STUDENT_NAME = "정헌진"

# OpenRouter — OpenAI SDK 호환 API (https://openrouter.ai)
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
AI_MODEL = "openrouter/free"

DEFAULT_QUESTION = "중학생에게 공부 팁 한 가지만 알려줘"
DEFAULT_SUBJECT = "영어 단어"

# ===== [🟡] 튜터 톤 — call_ai 에 system 으로 넣습니다 =====
TUTOR_PROMPT = "너는 중학생을 도와주는 친절한 튜터야. 쉽고 짧게 설명해 줘."


# ===== 4주차 OX (🔴 세 번째 탭에서 사용) =====
QUESTIONS = [
    {"text": "Python은 프로그래밍 언어이다.", "answer": "O"},
    {"text": "HTML은 데이터베이스이다.", "answer": "X"},
    {"text": "Flask는 Python 웹 프레임워크이다.", "answer": "O"},
]


def call_ai(question: str) -> str:
    """API 키는 Replit Secrets (OPENROUTER_API_KEY) — JS에는 키 없음!"""
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        return "⚠️ Replit Secrets에 OPENROUTER_API_KEY 를 설정해 주세요. (교사에게 문의)"

    messages = [
        # [🟡] system prompt — TUTOR_PROMPT 사용
        {"role": "system", "content": TUTOR_PROMPT},
        {"role": "user", "content": question},
    ]

    client = OpenAI(base_url=OPENROUTER_BASE_URL, api_key=api_key)
    response = client.chat.completions.create(
        model=AI_MODEL,
        messages=messages,
    )
    return response.choices[0].message.content or ""


def build_quiz_prompt(subject: str) -> str:
    return f"중학생용 {subject} 퀴즈 3문제를 OX 형식으로 만들어줘. 각 문제 뒤에 (정답: O 또는 X)를 적어줘."


def check_answer(q_index: int, user_answer: str) -> bool:
    if q_index < 0 or q_index >= len(QUESTIONS):
        return False
    return user_answer.upper() == QUESTIONS[q_index]["answer"]


@app.route("/")
def home():
    """한 페이지에 챗봇·퀴즈·(🔴) OX 탭."""
    return render_template(
        "index.html",
        app_title=APP_TITLE,
        name=STUDENT_NAME,
        default_question=DEFAULT_QUESTION,
        default_subject=DEFAULT_SUBJECT,
        questions=QUESTIONS,
    )

cache = {}
@app.route("/api/chat", methods=["POST"])
def api_chat():
    """5주차 — AI 챗."""
    data = request.get_json(silent=True) or {}
    question = (data.get("question") or "").strip() or DEFAULT_QUESTION
    if question in cache:
        reply = cache[question]
    else:
        reply = call_ai(question)
        cache[question] = reply
    return jsonify({"reply": reply, "question": question})

cache_quiz = {}
@app.route("/api/generate-quiz")
def api_generate_quiz():
    """6주차 — AI 퀴즈 생성."""
    subject = (request.args.get("subject") or "").strip() or DEFAULT_SUBJECT
    prompt = build_quiz_prompt(subject)
    if subject in cache_quiz:
        quiz = cache_quiz[subject]
    else:
        quiz = call_ai(prompt)
        cache_quiz[subject] = quiz
    return jsonify({"quiz": quiz, "subject": subject})


@app.route("/api/check")
def api_check():
    """4주차 — OX 채점 (🔴 세 번째 탭)."""
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
