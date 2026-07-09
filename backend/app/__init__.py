from flask import Flask

from app.config.config import Config
from app.extensions import db, migrate, bcrypt, jwt
from app import models
from app.models.role import Role
from app.models.user import User


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)

    @app.route("/")
    def home():
        return {
            "status": "success",
            "message": "Secure Online Voting API",
            "version": "1.0.0"
        }

    return app