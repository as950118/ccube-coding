"""
AI웹반 10주차 — 웹캠 + Teachable Machine (같은 Flask 앱 안에서)

[🟢] 이번 주: MODEL_URL 붙여넣기 → 웹캠 켜고 → 「분류하기」로 결과 확인!
[🟡] 「지금 뭐야?」 버튼으로 실시간(연속) 분류
[🔴] 확률 80% 이상일 때만 결과 강조

9주차 이미지 업로드 = 브라우저(JS)가 TM 호출
10주차 웹캠도 마찬가지 — Python은 여전히 API 키 없음!
카메라를 막았거나 카메라가 없으면 9주처럼 파일 업로드로 대체됩니다.
"""
import os

from flask import Flask, render_template

app = Flask(__name__)

STUDENT_NAME = "홍길동"
APP_TITLE = "이미지 AI 실험실 — 웹캠"

# ===== [🟢] Teachable Machine 모델 URL — 끝에 / 포함! =====
# 9주차와 같은 모델을 써도 되고, 새로 만들어도 됩니다.
# 예: https://teachablemachine.withgoogle.com/models/XXXXXXXX/
MODEL_URL = "https://teachablemachine.withgoogle.com/models/GFzCz0vn0/"


@app.route("/")
def home():
    """Flask는 페이지·MODEL_URL 만 전달 — 분류(웹캠 포함)는 브라우저 JS!"""
    return render_template(
        "index.html",
        name=STUDENT_NAME,
        app_title=APP_TITLE,
        model_url=MODEL_URL,
    )


# (선택) 별도 페이지
@app.route("/webcam-lab")
def webcam_lab():
    return home()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)
