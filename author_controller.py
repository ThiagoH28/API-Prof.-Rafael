from flask import Blueprint, request, jsonify
from app.services.author_service import AuthorService
from app.schemas.author_schema import AuthorSchema
from flask_jwt_extended import jwt_required

author_bp = Blueprint("author", __name__)
author_service = AuthorService()
author_schema = AuthorSchema()

@author_bp.route("/", methods=["POST"])
@jwt_required()
def create_author():
    data = request.get_json()
    validated_data = author_schema.validate(data)
    new_author = author_service.create_author(validated_data)
    return jsonify(new_author), 201

@author_bp.route("/", methods=["GET"])
def get_authors():
    name = request.args.get("name")
    if name:
        authors = author_service.get_authors_by_name(name)
    else:
        authors = author_service.get_all_authors()
    return jsonify(authors), 200

@author_bp.route("/<int:author_id>", methods=["PUT"])
@jwt_required()
def update_author(author_id):
    data = request.get_json()
    validated_data = author_schema.validate(data)
    updated_author = author_service.update_author(author_id, validated_data)
    return jsonify(updated_author), 200

@author_bp.route("/<int:author_id>", methods=["DELETE"])
@jwt_required()
def delete_author(author_id):
    author_service.delete_author(author_id)
    return jsonify({"message": "Author deleted successfully"}), 200
