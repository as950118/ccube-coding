# 3.2 시스템 지침(instructions): 역할·규칙·환각 방지 제약을 고정한다.
from openai import OpenAI

client = OpenAI()
MODEL = "gpt-4.1-mini"

system_prompt = (
    "너는 학교생활 도우미 '김반장'이야. "
    "오직 제공된 공지와 데이터에 근거해서만 답변해. "
    "공지에 명시되지 않은 날짜, 장소, 준비물은 절대로 추측하지 말고 '확인 필요'라고 표시해."
)

notice = "다음 체육 시간에는 운동화를 준비하세요. 비가 오면 교실에서 수업합니다."
prompt = f"아래 공지를 [일정 / 할 일 / 준비물] 순서로 정리해 줘.\n공지: {notice}"

response = client.responses.create(
    model=MODEL,
    instructions=system_prompt,
    input=prompt,
    temperature=0.2,  # 낮을수록 덜 창의적이고 더 일관된 답
)
print(response.output_text)

# 실험: instructions= 줄을 주석 처리하고 다시 실행해서, 날짜 정보가 없을 때 답이 어떻게 달라지는지 비교해 보자.
