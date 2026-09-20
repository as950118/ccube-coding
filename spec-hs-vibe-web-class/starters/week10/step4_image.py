# 4.2 이미지(멀티모달) 분석: 텍스트 프롬프트와 이미지를 한 메시지에 함께 담는다.
import base64

from openai import OpenAI

client = OpenAI()
MODEL = "gpt-4.1-mini"

IMAGE_FILE = "notice.jpg"   # PNG라면 파일명과 아래 MIME 타입을 함께 바꾼다
MIME_TYPE = "image/jpeg"    # JPG → image/jpeg, PNG → image/png

with open(IMAGE_FILE, "rb") as file:
    image_b64 = base64.b64encode(file.read()).decode("ascii")

prompt = (
    "이 시간표/안내문 사진을 분석해 줘. "
    "1) 전체 일정이나 시간표 목록을 텍스트로 표기하고, "
    "2) 챙겨야 할 준비물을 요약해 줘. "
    "글자가 흐려 식별할 수 없는 부분은 '확인 필요'라고 표시해."
)

response = client.responses.create(
    model=MODEL,
    input=[{
        "role": "user",
        "content": [
            {"type": "input_text", "text": prompt},
            {"type": "input_image", "image_url": f"data:{MIME_TYPE};base64,{image_b64}"},
        ],
    }],
)
print(response.output_text)
