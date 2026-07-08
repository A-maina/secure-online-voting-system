from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return {
            "status": "success",
            "message": "Secure Online Voting API",
            "version": "1.0.0"
        }

    return app