import pytest
from app import create_app, db
from app.models import Book

@pytest.fixture
def test_app():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(test_app):
    return test_app.test_client()

def test_create_book(client):
    response = client.post(
        "/books/",
        json={"title": "Test Book", "genre": "Fiction", "year": 2023, "available": True, "author_id": 1},
    )
    assert response.status_code == 201

def test_get_books(client):
    response = client.get("/books/")
    assert response.status_code == 200
