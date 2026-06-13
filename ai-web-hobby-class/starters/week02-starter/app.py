"""
AI웹반 2주차 — Python 변수를 HTML에 넘깁니다.

[🟢] 이번 주: app.py 의 변수 2~3개만 수정!
[🟡] static/style.css 로 색·배경 꾸미기
[3주~] Python 함수 + fetch API
[5주~] Python 이 AI API 를 호출합니다.
"""
import os

from flask import Flask, render_template

app = Flask(__name__)

# ===== [🟢] 여기만 바꾸세요 — Python 변수 =====
STUDENT_NAME = "홍길동"
INTRO = "안녕하세요! 중학교 2학년 홍길동입니다. Python과 AI, 웹을 같이 배우고 싶어요."
HOBBY = "축구"
FAVORITE = "피자 🍕"

# ===== [🔴] 도전: 좋아하는 음식 list → template 에서 for loop =====
# FAVORITE_FOODS = ["피자", "치킨", "떡볶이"]


@app.route("/")
def home():
    """Python 변수 → render_template → HTML {{ }} 로 표시."""
    return render_template(
        "index.html",
        name=STUDENT_NAME,
        intro=INTRO,
        hobby=HOBBY,
        favorite=FAVORITE,
        # favorite_foods=FAVORITE_FOODS,  # 🔴 주석 해제 후 template 도 수정
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
