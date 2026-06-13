"""
AI웹반 1주차 — Flask가 HTML 페이지를 보내줍니다.

[🟢] 이번 주: app.py 는 읽기만. templates/index.html 만 수정!
[2주~] Python 변수를 template {{ }} 로 넘깁니다.
[5주~] Python 이 AI API 를 호출합니다.
"""
import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    """브라우저가 '/' 를 요청하면 → index.html 을 보내줌."""
    return render_template("index.html")

@app.route("/hello")
def hello():
    return render_template("hello.html", name="정헌진", age="32")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)
