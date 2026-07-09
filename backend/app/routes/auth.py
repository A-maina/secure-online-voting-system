from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.middleware.role_required import role_required
from app.schemas.auth_schema import login_schema
from app.services.auth_service import authenticate_user

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/api/auth"
)


@auth_bp.get("/health")
def health():
    return {
        "status": "Authentication module is working"
    }


@auth_bp.post("/login")
def login():

    try:
        data = login_schema.load(request.get_json())

    except ValidationError as err:
        return jsonify(err.messages), 400

    result = authenticate_user(
        data["email"],
        data["password"]
    )

    if result is None:
        return jsonify({
            "message": "Invalid email or password."
        }), 401

    return jsonify(result), 200
@auth_bp.get("/profile")
@jwt_required()
def profile():

    return {
        "message": "Authenticated",
        "user_id": get_jwt_identity()
    }
@auth_bp.get("/admin")
@role_required("Administrator")
def admin_only():

    return {
        "message": "Welcome Administrator!"
    }