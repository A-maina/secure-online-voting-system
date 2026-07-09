from flask_jwt_extended import create_access_token

from app.extensions import bcrypt
from app.models.user import User


def hash_password(password):
    return bcrypt.generate_password_hash(password).decode("utf-8")


def verify_password(password, password_hash):
    return bcrypt.check_password_hash(password_hash, password)


def authenticate_user(email, password):
    user = User.query.filter_by(email=email).first()

    if not user:
        return None

    if not verify_password(password, user.password_hash):
        return None

    token = create_access_token(identity=str(user.user_id))

    return {
        "access_token": token,
        "user": {
            "id": user.user_id,
            "name": f"{user.first_name} {user.last_name}",
            "email": user.email
        }
    }