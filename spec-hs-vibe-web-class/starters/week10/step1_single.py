# 2.2 단일 대화: 질문 한 번 = 답변 한 번. 이전 대화는 전달되지 않는다.
from openai import OpenAI

# 환경 변수 OPENAI_API_KEY를 자동으로 읽는다. 키를 코드에 적지 않는다.
client = OpenAI()
MODEL = "gpt-4.1-mini"

response = client.responses.create(
    model=MODEL,
    input="학교생활을 돕는 반장봇의 핵심 기능 3가지를 bullet point로 추천해 줘.",
)
print(response.output_text)
