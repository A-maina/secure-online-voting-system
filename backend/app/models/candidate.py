from app.extensions import db
from app.models.base_model import BaseModel


class Candidate(BaseModel):
    __tablename__ = "candidates"

    candidate_id = db.Column(
        db.Integer,
        primary_key=True
    )

    election_id = db.Column(
        db.Integer,
        db.ForeignKey("elections.election_id"),
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

    manifesto = db.Column(
        db.Text
    )

    photo_url = db.Column(
        db.String(255)
    )

    is_active = db.Column(
        db.Boolean,
        default=True
    )

    election = db.relationship(
        "Election",
        back_populates="candidates"
    )
    votes = db.relationship(
    "Vote",
    back_populates="candidate",
    lazy=True
)

    def __repr__(self):
        return f"<Candidate {self.first_name} {self.last_name}>"