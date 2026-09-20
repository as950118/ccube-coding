# 2.3 연속 대화: 대화 기록(history)을 리스트로 직접 유지하고, 매번 함께 보낸다.
from openai import OpenAI

client = OpenAI()
MODEL = "gpt-4.1-mini"

history = []  # {"role": "user" | "assistant", "content": "..."} 를 차곡차곡 쌓는다

while True:
    question = input("나: ").strip()

    if question in ["exit", "종료"]:
        break
    if not question:
        continue
    if question == "초기화":
        history = []
        print("[시스템] 대화 문맥이 초기화되었습니다.")
        continue

    history.append({"role": "user", "content": question})
    response = client.responses.create(model=MODEL, input=history)  # 기록 전체를 보낸다
    answer = response.output_text
    history.append({"role": "assistant", "content": answer})
    print(f"AI: {answer}\n")
