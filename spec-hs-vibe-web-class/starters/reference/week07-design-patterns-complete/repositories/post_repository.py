from abc import ABC, abstractmethod


class PostRepository(ABC):
    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def find_by_id(self, post_id):
        pass

    @abstractmethod
    def save(self, title, content):
        pass

    @abstractmethod
    def update(self, post_id, title, content):
        pass

    @abstractmethod
    def delete(self, post_id):
        pass
