"""
AI웹반 3주차 — 완성 예시 (교사 시연용)
"""
import os

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

STUDENT_NAME = "김서연"


def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b


@app.route("/")
def home():
    return render_template("index.html", name=STUDENT_NAME)


@app.route("/api/add")
def api_add():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))

    if a == 0 and b == 0:
        return jsonify({"error": "숫자를 입력하세요"}), 400

    return jsonify({"sum": add(a, b)})


@app.route("/api/sub")
def api_sub():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))

    if a == 0 and b == 0:
        return jsonify({"error": "숫자를 입력하세요"}), 400

    return jsonify({"diff": subtract(a, b)})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
