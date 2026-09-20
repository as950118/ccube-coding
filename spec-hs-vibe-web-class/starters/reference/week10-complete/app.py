import base64
import os
import uuid

import openai
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request, session
from openai import OpenAI

import neis

load_dotenv()  # .env 파일이 있으면 환경 변수로 읽어 들인다 (PyCharm 실행 설정에 직접 넣어도 된다)

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-change-me")
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024  # 업로드 사진 5MB 제한

# 환경 변수 OPENAI_API_KEY를 자동으로 읽는다. 코드·화면·JS 어디에도 키를 쓰지 않는다.
client = OpenAI()
MODEL = os.environ.get("OPENAI_MODEL") or "gpt-4.1-mini"

SYSTEM_PROMPT = (
    "너는 학교생활 도우미 '김반장'이야. "
    "오직 제공된 공지와 데이터에 근거해서만 답변해. "
    "공지에 명시되지 않은 날짜, 장소, 준비물은 절대로 추측하지 말고 '확인 필요'라고 표시해."
)

IMAGE_MIME = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png"}

# 연속 대화: 사용자(브라우저 세션)마다 대화 기록 리스트를 따로 보관한다.
MAX_HISTORY = 20  # 최근 20개 메시지(질문+답변 10쌍)만 다시 보낸다
user_chats: dict[str, list[dict]] = {}


class AIError(Exception):
    """화면에 그대로 보여줄 수 있는 AI 호출 오류 메시지."""


def ask(user_input, instructions=SYSTEM_PROMPT) -> str:
    """OpenAI에 한 번 요청하고 텍스트 답변을 돌려준다.

    user_input이 문자열이면 단일 대화, 메시지 리스트면 대화 기록을 함께 보내는 연속 대화다.
    """
    try:
        response = client.responses.create(
            model=MODEL,
            instructions=instructions,  # 시스템 지침(역할·규칙·환각 방지)
            input=user_input,
            temperature=0.2,
        )
    except openai.AuthenticationError:
        raise AIError("API 키가 올바르지 않아요. OPENAI_API_KEY 환경 변수를 확인하세요.")
    except openai.RateLimitError:
        raise AIError("요청이 너무 많거나 사용 한도를 넘었어요. 잠시 뒤에 다시 시도하세요.")
    except openai.OpenAIError as e:
        raise AIError(f"AI 호출 중 오류가 났어요. ({type(e).__name__})")
    return response.output_text


def get_user_key() -> str:
    if "user_key" not in session:
        session["user_key"] = str(uuid.uuid4())
    return session["user_key"]


def chat_with_history(user_key: str, message: str) -> str:
    history = user_chats.setdefault(user_key, [])
    history.append({"role": "user", "content": message})
    try:
        reply = ask(history)
    except AIError:
        history.pop()  # 실패한 질문은 기록에서 뺀다
        raise
    history.append({"role": "assistant", "content": reply})
    del history[:-MAX_HISTORY]
    return reply


def brief_meal(school_name: str, meal: dict) -> str:
    """급식 원문(근거 데이터)을 먼저 주고, 그 안에서만 해설하게 한다 — Grounding."""
    allergy_table = ", ".join(f"{n}.{name}" for n, name in neis.ALLERGY_CODES.items())
    prompt = (
        f"아래는 나이스(NEIS) 공식 API에서 가져온 {school_name}의 오늘 {meal['meal_name']} 원문이야.\n"
        "이 원문에만 근거해서 답하고, 원문에 없는 메뉴·수치는 지어내지 말고 '확인 필요'라고 써.\n"
        f"[알레르기 번호표] {allergy_table}\n"
        f"[메뉴 원문]\n{meal['menu']}\n"
        f"[칼로리] {meal['calorie'] or '정보 없음'}\n"
        f"[영양정보]\n{meal['nutrition'] or '정보 없음'}\n\n"
        "1) 오늘 급식을 1~2문장으로 요약해줘.\n"
        "2) 메뉴 뒤 괄호 숫자는 알레르기 번호야. 번호표로 풀이해서 주의할 메뉴를 알려줘.\n"
        "3) 칼로리·영양정보가 있으면 짧게 해설해줘.\n"
        "마크다운 기호(#, *, **)는 쓰지 말고 일반 문장과 줄바꿈으로만 써."
    )
    return ask(prompt)


def summarize_notice(notice: str) -> str:
    """단일 대화: 이전 요청은 전혀 전달되지 않는다(Stateless)."""
    prompt = (
        "아래 공지를 [일정 / 할 일 / 준비물] 순서로 간결하게 정리해줘.\n"
        "공지에 없는 항목은 '확인 필요'라고 써. 마크다운 기호는 쓰지 마.\n"
        f"공지: {notice}"
    )
    return ask(prompt)


def analyze_image(file_storage) -> str:
    ext = os.path.splitext(file_storage.filename or "")[1].lower()
    mime = IMAGE_MIME.get(ext)
    if mime is None:
        raise AIError("JPG 또는 PNG 사진만 올릴 수 있어요.")

    image_b64 = base64.b64encode(file_storage.read()).decode("ascii")
    prompt = (
        "이 시간표/안내문 사진을 분석해 줘. "
        "1) 전체 일정이나 시간표 목록을 텍스트로 표기하고, "
        "2) 챙겨야 할 준비물을 요약해 줘. "
        "글자가 흐려 식별할 수 없는 부분은 '확인 필요'라고 표시하고, 사진에 없는 내용은 절대 지어내지 마. "
        "마크다운 기호는 쓰지 마."
    )
    # 텍스트 + 이미지를 한 메시지의 content 리스트에 함께 담는다
    message = [{
        "role": "user",
        "content": [
            {"type": "input_text", "text": prompt},
            {"type": "input_image", "image_url": f"data:{mime};base64,{image_b64}"},
        ],
    }]
    return ask(message)


@app.route("/", methods=["GET", "POST"])
def index():
    user_key = get_user_key()
    view = {
        "school_name": "", "meal_school": None, "meal": None, "ai_meal": None,
        "notice_text": "", "summary": None, "image_result": None, "errors": {},
    }

    if request.method == "POST":
        action = request.form.get("action")

        if action == "meal":
            view["school_name"] = request.form.get("school_name", "").strip()
            school = neis.get_school_code(view["school_name"]) if view["school_name"] else None
            if school is None:
                view["errors"]["meal"] = "학교를 찾지 못했어요. 정확한 학교 이름(예: 경기고등학교)을 입력하세요."
            else:
                office_code, school_code, school_full_name = school
                view["meal_school"] = school_full_name
                view["meal"] = neis.get_today_meal(office_code, school_code)
                if view["meal"] is None:
                    view["errors"]["meal"] = "오늘 급식 정보가 등록되지 않았습니다. (주말·방학·휴업일일 수 있어요)"
                else:
                    try:
                        view["ai_meal"] = brief_meal(school_full_name, view["meal"])
                    except AIError as e:
                        view["errors"]["ai_meal"] = str(e)  # 원문은 그대로 보여준다

        elif action == "notice":
            view["notice_text"] = request.form.get("notice_text", "").strip()
            if not view["notice_text"]:
                view["errors"]["notice"] = "공지 내용을 입력하세요."
            else:
                try:
                    view["summary"] = summarize_notice(view["notice_text"])
                except AIError as e:
                    view["errors"]["notice"] = str(e)

        elif action == "image":
            photo = request.files.get("photo")
            if photo is None or photo.filename == "":
                view["errors"]["image"] = "사진 파일을 선택하세요."
            else:
                try:
                    view["image_result"] = analyze_image(photo)
                except AIError as e:
                    view["errors"]["image"] = str(e)

    return render_template("index.html", history=user_chats.get(user_key, []), **view)


@app.route("/chat", methods=["POST"])
def chat():
    user_key = get_user_key()
    message = request.form.get("message", "").strip()

    if not message:
        return jsonify({"reply": "질문을 입력하세요."}), 400
    if message == "초기화":
        user_chats.pop(user_key, None)
        return jsonify({"reply": "[시스템] 대화 문맥이 초기화되었습니다."})

    try:
        return jsonify({"reply": chat_with_history(user_key, message)})
    except AIError as e:
        return jsonify({"reply": str(e)}), 502


@app.errorhandler(413)
def too_large(_):
    return "사진 용량이 너무 커요(5MB 이하). 뒤로 가서 작은 사진을 올려주세요.", 413


if __name__ == "__main__":
    app.run(debug=True, port=5001)
