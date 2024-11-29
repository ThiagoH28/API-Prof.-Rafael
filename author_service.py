from app.repositories.author_repository import AuthorRepository

class AuthorService:
    def __init__(self):
        self.author_repository = AuthorRepository()

    def create_author(self, data):
        return self.author_repository.create(data)

    def get_all_authors(self):
        return self.author_repository.get_all()

    def get_authors_by_name(self, name):
        return self.author_repository.get_by_name(name)

    def update_author(self, author_id, data):
        if not self.author_repository.get_by_id(author_id):
            raise ValueError("Author not found")
        return self.author_repository.update(author_id, data)

    def delete_author(self, author_id):
        if not self.author_repository.get_by_id(author_id):
            raise ValueError("Author not found")
        self.author_repository.delete(author_id)
