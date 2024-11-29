from flask import Blueprint, request, jsonify
from app.services.user_service import UserService
from app.schemas.user_schema import UserSchema
from flask_jwt_extended import create_access_token, jwt_required

user_bp = Blueprint("user", __name__)
user_service = UserService()
user_schema = UserSchema()

@user_bp.route("/register", methods=["POST"])
def register_user():
    data = request.get_json()
    validated_data = user_schema.validate(data)
    new_user = user_service.register_user(validated_data)
    return jsonify(new_user), 201

@user_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = user_service.authenticate(data["email"], data["password"])
    if user:
        token = create_access_token(identity=user["id"])
        return jsonify({"access_token": token}), 200
    return jsonify({"error": "Invalid credentials"}), 401

@user_bp.route("/<int:user_id>", methods=["GET"])
@jwt_required()
def get_user(user_id):
    user = user_service.get_user(user_id)
    return jsonify(user), 200
