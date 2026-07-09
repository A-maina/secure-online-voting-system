from flask import Blueprint, request, jsonify

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

    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({
            "message": "Email and password are required."
        }), 400

    result = authenticate_user(email, password)

    if result is None:
        return jsonify({
            "message": "Invalid email or password."
        }), 401

    return jsonify(result), 200