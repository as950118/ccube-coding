from models.post import Post
from repositories.post_repository import PostRepository


class MemoryPostRepository(PostRepository):
    def __init__(self):
        self._posts = []
        self._next_id = 1

    def find_all(self):
        return list(reversed(self._posts))

    def find_by_id(self, post_id):
        return next((p for p in self._posts if p.id == post_id), None)

    def save(self, title, content):
        self._posts.append(Post(self._next_id, title, content, "방금"))
        self._next_id += 1

    def update(self, post_id, title, content):
        post = self.find_by_id(post_id)
        if post:
            post.title = title
            post.content = content

    def delete(self, post_id):
        self._posts = [p for p in self._posts if p.id != post_id]
