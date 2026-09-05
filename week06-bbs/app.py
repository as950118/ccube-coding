from flask import Flask, request, render_template, redirect, url_for
from sqlite3
from pathlib import Path

@app.route("/")
def index():
 conn = get_db()
 posts = conn.execute(
 "SELECT * FROM posts ORDER BY id DESC"
 ).fetchall()
 conn.close()
 return render_template("list.html", posts=posts)

@app.route("/posts/<int:post_id>")
def detail(post_id):
 conn = get_db()
 post = conn.execute(
 "SELECT * FROM posts WHERE id = ?", (post_id,)
 ).fetchone()
 conn.close()
 return render_template("detail.html", post=post)

@app.route("/new")
def new_form():
 return render_template("new.html")

@app.route("/posts", methods=["POST"])
def create_post():
 title = request.form.get("title", "").strip()
 content = request.form.get("content", "").strip()

 conn = get_db()
 conn.execute(
 "INSERT INTO posts (title, content) VALUES (?, ?)",
 (title, content)
 )
 conn.commit()
 conn.close()
 return redirect(url_for("index"))

if __name__ == "__main__":
    create_table()
    app.run(debug=True, port=5001)