"""
AI웹반 2주차 — 완성 예시 (교사 시연용)
"""
import os

from flask import Flask, render_template

app = Flask(__name__)

STUDENT_NAME = "김서연"
INTRO = "안녕하세요! 중학교 1학년 김서연이에요. AI와 웹을 배워서 나만의 학습 도우미를 만들고 싶어요."
HOBBY = "그림 그리기"
FAVORITE = "고양이 🐱"
FAVORITE_FOODS = ["피자", "떡볶이", "아이스크림"]


@app.route("/")
def home():
    return render_template(
        "index.html",
        name=STUDENT_NAME,
        intro=INTRO,
        hobby=HOBBY,
        favorite=FAVORITE,
        favorite_foods=FAVORITE_FOODS,
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
