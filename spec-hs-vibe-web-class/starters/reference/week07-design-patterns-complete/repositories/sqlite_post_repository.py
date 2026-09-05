import sqlite3

from models.post import Post
from repositories.post_repository import PostRepository


class SqlitePostRepository(PostRepository):
    def __init__(self, db_path):
        self.db_path = db_path

    def _get_db(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def create_table(self):
        conn = self._get_db()
        conn.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TEXT DEFAULT (datetime('now', 'localtime'))
            )
        """)
        conn.commit()
        conn.close()

    def find_all(self):
        conn = self._get_db()
        rows = conn.execute(
            "SELECT * FROM posts ORDER BY id DESC"
        ).fetchall()
        conn.close()
        return [
            Post(r["id"], r["title"], r["content"], r["created_at"])
            for r in rows
        ]

    def find_by_id(self, post_id):
        conn = self._get_db()
        row = conn.execute(
            "SELECT * FROM posts WHERE id = ?", (post_id,)
        ).fetchone()
        conn.close()
        if row is None:
            return None
        return Post(row["id"], row["title"], row["content"], row["created_at"])

    def save(self, title, content):
        conn = self._get_db()
        conn.execute(
            "INSERT INTO posts (title, content) VALUES (?, ?)",
            (title, content)
        )
        conn.commit()
        conn.close()

    def update(self, post_id, title, content):
        conn = self._get_db()
        conn.execute(
            "UPDATE posts SET title = ?, content = ? WHERE id = ?",
            (title, content, post_id)
        )
        conn.commit()
        conn.close()

    def delete(self, post_id):
        conn = self._get_db()
        conn.execute("DELETE FROM posts WHERE id = ?", (post_id,))
        conn.commit()
        conn.close()
