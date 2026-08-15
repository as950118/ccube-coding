"""
AI웹반 9주차 — Teachable Machine: 두 번째 AI (이미지)

[🟢] 이번 주: MODEL_URL 붙여넣기 → 이미지 업로드 → 분류 결과!
[🟡] 클래스명 한글로 표시
[🔴] 확률 % 표시
[10주~] 웹캠 + TM

텍스트 AI(5~8주) = Python이 호출
이미지 AI(9~10주) = 브라우저(JS)가 호출 — API 키 없음!
"""
import os

from flask import Flask, render_template

app = Flask(__name__)

STUDENT_NAME = "홍길동"
APP_TITLE = "이미지 AI 실험실"

# ===== [🟢] Teachable Machine 모델 URL — 끝에 / 포함! =====
# 교사/학생이 https://teachablemachine.withgoogle.com 에서 만든 모델
# 예: https://teachablemachine.withgoogle.com/models/XXXXXXXX/
MODEL_URL = "https://teachablemachine.withgoogle.com/models/GFzCz0vn0/" # 걸그룹 분류기


@app.route("/")
def home():
    """Flask는 페이지·MODEL_URL 만 전달 — 분류는 브라우저 JS!"""
    return render_template(
        "index.html",
        name=STUDENT_NAME,
        app_title=APP_TITLE,
        model_url=MODEL_URL,
    )


# (선택) 별도 페이지
@app.route("/image-lab")
def image_lab():
    return home()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)
