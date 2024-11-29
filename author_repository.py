from app.models import Author, db

class AuthorRepository:
    def get_by_id(self, author_id):
        return Author.query.get(author_id)

    def get_all(self):
        return Author.query.all()

    def get_by_name(self, name):
        return Author.query.filter(Author.name.ilike(f"%{name}%")).all()

    def create(self, data):
        new_author = Author(**data)
        db.session.add(new_author)
        db.session.commit()
        return new_author

    def update(self, author_id, data):
        author = self.get_by_id(author_id)
        for key, value in data.items():
            setattr(author, key, value)
        db.session.commit()
        return author

    def delete(self, author_id):
        author = self.get_by_id(author_id)
        db.session.delete(author)
        db.session.commit()
