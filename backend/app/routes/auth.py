from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

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