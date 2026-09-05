class Post:
    def __init__(self, id, title, content, created_at=None):
        self.id = id
        self.title = title
        self.content = content
        self.created_at = created_at
