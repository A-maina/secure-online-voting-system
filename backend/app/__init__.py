from flask import Flask
from sqlalchemy import text

from app.routes.auth import auth_bp
from app.config.config import Config
from app.extensions import db, migrate, bcrypt, jwt
from app.routes.election import election_bp
from app.routes.candidate import candidate_bp

from app import models



def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    app.register_blueprint(auth_bp)
    app.register_blueprint(election_bp)
    app.register_blueprint(candidate_bp)


    db.init_app(app)
    
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)
    with app.app_context():
     try:
        db.session.execute(text("SELECT 1"))
        print("✅ Database connection successful.")
     except Exception as e:
        print(f"❌ Database connection failed: {e}")

    @app.route("/")
    def home():
        return {
            "status": "success",
            "message": "Secure Online Voting API",
            "version": "1.0.0"
        }

    return app