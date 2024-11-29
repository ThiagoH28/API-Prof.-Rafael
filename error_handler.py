from flask import jsonify

class APIException(Exception):
    def __init__(self, message, status_code):
        self.message = message
        self.status_code = status_code

def register_error_handlers(app):
    @app.errorhandler(APIException)
    def handle_api_exception(error):
        response = {
            "error": error.message,
            "status_code": error.status_code
        }
        return jsonify(response), error.status_code

    @app.errorhandler(400)
    def handle_bad_request(e):
        return jsonify({"error": "Bad request", "status_code": 400}), 400

    @app.errorhandler(404)
    def handle_not_found(e):
        return jsonify({"error": "Resource not found", "status_code": 404}), 404

    @app.errorhandler(500)
    def handle_server_error(e):
        return jsonify({"error": "Internal server error", "status_code": 500}), 500
