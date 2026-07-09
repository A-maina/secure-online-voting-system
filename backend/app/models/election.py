from app.extensions import db
from app.models.base_model import BaseModel


class Election(BaseModel):
    __tablename__ = "elections"

    election_id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(150),
        nullable=False
    )

    description = db.Column(
        db.Text
    )

    start_date = db.Column(
        db.DateTime,
        nullable=False
    )

    end_date = db.Column(
        db.DateTime,
        nullable=False
    )

    status = db.Column(
        db.String(20),
        nullable=False,
        default="Draft"
    )

    candidates = db.relationship(
        "Candidate",
        back_populates="election",
        lazy=True
    )

    votes = db.relationship(
        "Vote",
        back_populates="election",
        lazy=True
    )

    def __repr__(self):
        return f"<Election {self.title}>"