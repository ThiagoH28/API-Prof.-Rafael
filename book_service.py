from app.repositories.book_repository import BookRepository
from app.repositories.author_repository import AuthorRepository

class BookService:
    def __init__(self):
        self.book_repository = BookRepository()
        self.author_repository = AuthorRepository()

    def create_book(self, data):
        author_id = data.get("author_id")
        if not self.author_repository.get_author_by_id(author_id):
            raise ValueError("Author does not exist")
        return self.book_repository.create(data)

    def get_all_books(self):
        return self.book_repository.get_all()

    def get_books_by_title(self, title):
        return self.book_repository.get_by_title(title)

    def update_book(self, book_id, data):
        if not self.book_repository.get_by_id(book_id):
            raise ValueError("Book not found")
        return self.book_repository.update(book_id, data)

    def delete_book(self, book_id):
        if not self.book_repository.get_by_id(book_id):
            raise ValueError("Book not found")
        self.book_repository.delete(book_id)
