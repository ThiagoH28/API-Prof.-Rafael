from flask import Blueprint, request, jsonify
from app.services.book_service import BookService
from app.schemas.book_schema import BookSchema
from flask_jwt_extended import jwt_required

book_bp = Blueprint("book", __name__)
book_service = BookService()
book_schema = BookSchema()

@book_bp.route("/", methods=["POST"])
@jwt_required()
def create_book():
    data = request.get_json()
    validated_data = book_schema.validate(data)
    new_book = book_service.create_book(validated_data)
    return jsonify(new_book), 201

@book_bp.route("/", methods=["GET"])
def get_books():
    title = request.args.get("title")
    if title:
        books = book_service.get_books_by_title(title)
    else:
        books = book_service.get_all_books()
    return jsonify(books), 200

@book_bp.route("/<int:book_id>", methods=["PUT"])
@jwt_required()
def update_book(book_id):
    data = request.get_json()
    validated_data = book_schema.validate(data)
    updated_book = book_service.update_book(book_id, validated_data)
    return jsonify(updated_book), 200

@book_bp.route("/<int:book_id>", methods=["DELETE"])
@jwt_required()
def delete_book(book_id):
    book_service.delete_book(book_id)
    return jsonify({"message": "Book deleted successfully"}), 200
