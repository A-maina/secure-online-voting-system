from datetime import datetime

from app.extensions import db


class BaseModel(db.Model):
    """
    Abstract base model providing common timestamp fields.
    """

    __abstract__ = True

    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    updated_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )