from app.extensions import db
from app.models.base_model import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)

    registration_number = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    first_name = db.Column(
        db.String(100),
        nullable=False
    )

    last_name = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(150),
        unique=True,
        nullable=False
    )

    password_hash = db.Column(
        db.String(255),
        nullable=False
    )

    role_id = db.Column(
        db.Integer,
        db.ForeignKey("roles.role_id"),
        nullable=False
    )

    is_active = db.Column(
        db.Boolean,
        default=True
    )

    has_voted = db.Column(
        db.Boolean,
        default=False
    )

    role = db.relationship(
        "Role",
        back_populates="users"
    )
    votes = db.relationship(
    "Vote",
    back_populates="user",
    lazy=True
)

    def __repr__(self):
        return f"<User {self.email}>"