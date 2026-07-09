from app.extensions import db
from app.models.base_model import BaseModel


class Role(BaseModel):
    __tablename__ = "roles"

    role_id = db.Column(db.Integer, primary_key=True)

    role_name = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    description = db.Column(
        db.String(255)
    )

    users = db.relationship(
        "User",
        back_populates="role"
    )

    def __repr__(self):
        return f"<Role {self.role_name}>"