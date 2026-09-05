from flask import Flask, request, render_template, redirect, url_for
import sqlite3
from pathlib import Path

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / "bbs.db"


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()


@app.route("/")
def index():
    # TODO: posts 테이블에서 전체 글을 최신순으로 조회해서 list.html에 넘기기
    # 힌트: SELECT * FROM posts ORDER BY id DESC
    pass


@app.route("/posts/<int:post_id>")
def detail(post_id):
    # TODO: id로 글 하나를 조회해서 detail.html에 넘기기
    # 힌트: SELECT * FROM posts WHERE id = ?
    pass


@app.route("/new")
def new_form():
    # TODO: new.html 보여주기
    pass


@app.route("/posts", methods=["POST"])
def create_post():
    # TODO: 폼에서 title, content를 꺼내 posts 테이블에 저장하고 목록(index)으로 이동
    # 힌트: INSERT INTO posts (title, content) VALUES (?, ?)
    pass


@app.route("/posts/<int:post_id>/edit")
def edit_form(post_id):
    # TODO: id로 글을 조회해서 edit.html에 기존 값을 채워 보여주기
    pass


@app.route("/posts/<int:post_id>/edit", methods=["POST"])
def update_post(post_id):
    # TODO: 폼 값으로 해당 글을 수정하고 상세(detail) 화면으로 이동
    # 힌트: UPDATE posts SET title = ?, content = ? WHERE id = ?
    pass


@app.route("/posts/<int:post_id>/delete", methods=["POST"])
def delete_post(post_id):
    # TODO: 해당 글을 삭제하고 목록(index)으로 이동
    # 힌트: DELETE FROM posts WHERE id = ?
    pass


if __name__ == "__main__":
    create_table()
    app.run(debug=True, port=5001)
