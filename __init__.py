from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from python_utils.logger import setup_logger
from app.utils.error_handler import register_error_handlers
from flask_swagger_ui import get_swaggerui_blueprint



db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///biblioteca.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = "your_jwt_secret_key"

    db.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        db.create_all()

    # Register blueprints (controllers)
    from app.controllers.book_controller import book_bp
    from app.controllers.author_controller import author_bp
    from app.controllers.user_controller import user_bp

    app.register_blueprint(book_bp, url_prefix="/books")
    app.register_blueprint(author_bp, url_prefix="/authors")
    app.register_blueprint(user_bp, url_prefix="/users")

    # Swagger UI setup
    swagger_ui = get_swaggerui_blueprint("/swagger", "/static/swagger.json")
    app.register_blueprint(swagger_ui, url_prefix="/swagger")

    # Setup logger and error handlers
    setup_logger(app)
    register_error_handlers(app)

    return app
