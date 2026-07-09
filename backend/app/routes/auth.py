from flask import Blueprint

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")


@auth_bp.get("/health")
def health():
    return {
        "status": "Authentication module is working"
    }, 200