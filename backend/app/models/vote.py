from app.extensions import db
from app.models.base_model import BaseModel


class Vote(BaseModel):
    __tablename__ = "votes"

    __table_args__ = (
        db.UniqueConstraint(
            "user_id",
            "election_id",
            name="uq_user_election_vote"
        ),
    )

    vote_id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.user_id"),
        nullable=False
    )

    election_id = db.Column(
        db.Integer,
        db.ForeignKey("elections.election_id"),
        nullable=False
    )

    candidate_id = db.Column(
        db.Integer,
        db.ForeignKey("candidates.candidate_id"),
        nullable=False
    )

    user = db.relationship(
        "User",
        back_populates="votes"
    )

    election = db.relationship(
        "Election",
        back_populates="votes"
    )

    candidate = db.relationship(
        "Candidate",
        back_populates="votes"
    )

    def __repr__(self):
        return (
            f"<Vote User:{self.user_id} "
            f"Candidate:{self.candidate_id}>"
        )