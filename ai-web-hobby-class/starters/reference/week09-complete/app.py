"""
AI웹반 9주차 — 완성 예시 (교사 시연용)
확률 % 표시 + 한글 라벨 매핑 포함
"""
import os

from flask import Flask, render_template

app = Flask(__name__)

STUDENT_NAME = "김서연"
APP_TITLE = "서연의 이미지 AI 실험실"

# 교사가 만든 공개 모델 URL로 교체해 시연
MODEL_URL = "https://teachablemachine.withgoogle.com/models/YOUR_MODEL_ID/"


@app.route("/")
def home():
    return render_template(
        "index.html",
        name=STUDENT_NAME,
        app_title=APP_TITLE,
        model_url=MODEL_URL,
    )


@app.route("/image-lab")
def image_lab():
    return home()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)
