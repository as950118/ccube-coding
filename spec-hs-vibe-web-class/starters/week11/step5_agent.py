# 실습 1. 에이전트 루프를 눈으로 보기
# 에이전트 = 모델(생각) + 도구(행동) + 루프(반복). 이 파일 전체가 아주 작은 "하네스"다.
import json
import os
from datetime import datetime

import openai
from dotenv import load_dotenv
from openai import OpenAI

import neis

load_dotenv()  # .env 파일이 있으면 환경 변수로 읽어 들인다

client = OpenAI()  # 환경 변수 OPENAI_API_KEY를 자동으로 읽는다
MODEL = os.environ.get("OPENAI_MODEL") or "gpt-4.1-mini"
MAX_STEPS = 5  # 루프 최대 횟수. 끝없이 도구를 부르며 돈을 쓰지 않도록 하네스가 정하는 안전장치

today = datetime.now()
INSTRUCTIONS = (
    "너는 학교생활 도우미 '김반장' 에이전트야. "
    "급식과 학사일정은 기억이나 추측으로 답하지 말고 반드시 도구로 조회한 결과만 사용해. "
    "질문에 답하려면 도구를 여러 번, 순서대로 써도 된다. "
    "도구 결과에 없는 내용은 '확인 필요'라고 써. 마크다운 기호(#, *, **)는 쓰지 마. "
    f"오늘 날짜는 {today:%Y년 %m월 %d일} ({'월화수목금토일'[today.weekday()]}요일)이야."
)

# ── 도구 설명서: 모델은 이 설명만 보고 "언제, 어떤 값으로" 부를지 스스로 정한다 ──
TOOLS = [
    {
        "type": "function",
        "name": "get_school_meal",
        "description": "나이스(NEIS) 공식 데이터에서 학교의 특정 날짜 급식(중식) 메뉴를 조회한다.",
        "parameters": {
            "type": "object",
            "properties": {
                "school_name": {"type": "string", "description": "학교 이름 (예: 서울과학고등학교)"},
                "date": {"type": "string", "description": "조회할 날짜 YYYYMMDD"},
            },
            "required": ["school_name", "date"],
        },
    },
    # TODO(실습 1-2): Claude Code에게 부탁해 "get_school_schedule" 도구 설명서를 여기에 추가한다.
]


# ── 도구의 실제 실행: 모델은 요청만 하고, 실행은 우리 코드가 한다 ──
def get_school_meal(school_name: str, date: str) -> dict:
    school = neis.get_school_code(school_name)
    if school is None:
        return {"error": "학교를 찾지 못함"}
    meal = neis.get_meal(school[0], school[1], date)
    if meal is None:
        return {"error": f"{date} 급식 정보 없음(주말·방학·휴업일일 수 있음)"}
    return {"school": school[2], "date": date, "menu": meal["menu"]}


# TODO(실습 1-2): neis.get_schedule()을 쓰는 get_school_schedule() 함수를 추가한다.


TOOL_FUNCTIONS = {
    "get_school_meal": get_school_meal,
    # TODO(실습 1-2): 새 도구를 여기에도 등록한다.
}


def run_tool(name: str, arguments: str) -> str:
    func = TOOL_FUNCTIONS.get(name)
    if func is None:
        return json.dumps({"error": f"없는 도구: {name}"}, ensure_ascii=False)
    try:
        result = func(**json.loads(arguments))
    except (TypeError, ValueError):
        result = {"error": "도구에 넘긴 값이 올바르지 않음"}
    return json.dumps(result, ensure_ascii=False)


# ── 에이전트 루프: 생각 → 행동 → 관찰을 답이 나올 때까지 반복 ──
def run_agent(question: str) -> str:
    work = [{"role": "user", "content": question}]
    for step in range(1, MAX_STEPS + 1):
        print(f"\n🧠 [{step}단계] 모델에게 묻는 중...")
        response = client.responses.create(
            model=MODEL, instructions=INSTRUCTIONS, input=work, tools=TOOLS, temperature=0.2,
        )
        calls = [item for item in response.output if item.type == "function_call"]
        if not calls:  # 도구를 부르지 않았다 = 최종 답을 냈다
            return response.output_text

        work += response.output
        for call in calls:
            print(f"🔧 도구 요청: {call.name}({call.arguments})")
            output = run_tool(call.name, call.arguments)
            print(f"👀 결과: {output[:200]}")
            work.append({"type": "function_call_output", "call_id": call.call_id, "output": output})
    return f"{MAX_STEPS}단계 안에 답을 못 찾았어요. 질문을 더 구체적으로 해 주세요."


if __name__ == "__main__":
    print("김반장 에이전트 (종료: exit)")
    while True:
        question = input("\n나: ").strip()
        if question in ["exit", "종료"]:
            break
        if not question:
            continue
        try:
            print(f"\n✅ 답: {run_agent(question)}")
        except openai.AuthenticationError:
            print("API 키가 올바르지 않아요. OPENAI_API_KEY 환경 변수를 확인하세요.")
        except openai.RateLimitError:
            print("요청이 너무 많거나 사용 한도(크레딧)를 넘었어요. 선생님께 알려 주세요.")
