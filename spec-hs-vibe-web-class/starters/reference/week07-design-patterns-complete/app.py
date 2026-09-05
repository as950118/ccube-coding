from flask import Flask, request, render_template, redirect, url_for, jsonify

from repositories.sqlite_post_repository import SqlitePostRepository

app = Flask(__name__)
repo = SqlitePostRepository("bbs.db")  # <- DI: 여기서 딱 한 번 조립


@app.route("/")
def index():
    posts = repo.find_all()
    return render_template("list.html", posts=posts)


@app.route("/posts/<int:post_id>")
def detail(post_id):
    post = repo.find_by_id(post_id)
    return render_template("detail.html", post=post)


@app.route("/new")
def new_form():
    return render_template("new.html")


@app.route("/posts", methods=["POST"])
def create_post():
    repo.save(
        request.form.get("title", "").strip(),
        request.form.get("content", "").strip()
    )
    return redirect(url_for("index"))


@app.route("/posts/<int:post_id>/edit")
def edit_form(post_id):
    post = repo.find_by_id(post_id)
    return render_template("edit.html", post=post)


@app.route("/posts/<int:post_id>/edit", methods=["POST"])
def update_post(post_id):
    repo.update(
        post_id,
        request.form.get("title", "").strip(),
        request.form.get("content", "").strip()
    )
    return redirect(url_for("detail", post_id=post_id))


@app.route("/posts/<int:post_id>/delete", methods=["POST"])
def delete_post(post_id):
    repo.delete(post_id)
    return redirect(url_for("index"))


# ===== 🔴 도전 과제(6주차에서 이어옴): 검색 =====
@app.route("/search")
def search():
    query = request.args.get("q", "").strip()
    posts = [p for p in repo.find_all() if query in p.title]
    return render_template("list.html", posts=posts)


# ===== 🔴 도전 과제: React 목록 화면용 JSON API =====
@app.route("/api/posts")
def api_posts():
    posts = repo.find_all()
    return jsonify([
        {"id": p.id, "title": p.title, "created_at": p.created_at}
        for p in posts
    ])


if __name__ == "__main__":
    repo.create_table()
    app.run(debug=True, port=5001)
