from app.models import Book, db

class BookRepository:
    def get_by_id(self, book_id):
        return Book.query.get(book_id)

    def get_all(self):
        return Book.query.all()

    def get_by_title(self, title):
        return Book.query.filter(Book.title.ilike(f"%{title}%")).all()

    def create(self, data):
        new_book = Book(**data)
        db.session.add(new_book)
        db.session.commit()
        return new_book

    def update(self, book_id, data):
        book = self.get_by_id(book_id)
        for key, value in data.items():
            setattr(book, key, value)
        db.session.commit()
        return book

    def delete(self, book_id):
        book = self.get_by_id(book_id)
        db.session.delete(book)
        db.session.commit()
