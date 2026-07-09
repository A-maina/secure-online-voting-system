from flask_jwt_extended import create_access_token

from app.extensions import bcrypt
from app.models.user import User


def hash_password(password):
    return bcrypt.generate_password_hash(password).decode("utf-8")


def verify_password(password, password_hash):
    return bcrypt.check_password_hash(password_hash, password)


def authenticate_user(email, password):
    user = User.query.filter_by(email=email).first()

    if user is None:
        return None

    if not verify_password(password, user.password_hash):
        return None

    access_token = create_access_token(
        identity=str(user.user_id),
        additional_claims={
            "role": user.role.role_name
        }
    )

    return {
        "access_token": access_token,
        "user": {
            "id": user.user_id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "role": user.role.role_name
        }
    }