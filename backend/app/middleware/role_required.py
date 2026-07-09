from functools import wraps

from flask import jsonify
from flask_jwt_extended import get_jwt, verify_jwt_in_request


def role_required(role_name):
    """
    Restrict access to users with a specific role.
    """

    def decorator(fn):

        @wraps(fn)
        def wrapper(*args, **kwargs):

            verify_jwt_in_request()

            claims = get_jwt()

            if claims.get("role") != role_name:
                return jsonify({
                    "message": "Access denied."
                }), 403

            return fn(*args, **kwargs)

        return wrapper

    return decorator