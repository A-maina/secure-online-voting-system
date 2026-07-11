from app.extensions import db
from app.models.candidate import Candidate


def create_candidate(data):
    candidate = Candidate(
        election_id=data["election_id"],
        first_name=data["first_name"],
        last_name=data["last_name"],
        manifesto=data.get("manifesto"),
        photo_url=data.get("photo_url")
    )

    db.session.add(candidate)
    db.session.commit()

    return candidate


def get_all_candidates():
    return Candidate.query.order_by(
        Candidate.candidate_id.desc()
    ).all()


def get_candidate(candidate_id):
    return Candidate.query.get_or_404(candidate_id)


def update_candidate(candidate_id, data):
    candidate = Candidate.query.get_or_404(candidate_id)

    candidate.first_name = data["first_name"]
    candidate.last_name = data["last_name"]
    candidate.manifesto = data.get("manifesto")
    candidate.photo_url = data.get("photo_url")
    candidate.election_id = data["election_id"]

    db.session.commit()

    return candidate


def delete_candidate(candidate_id):
    candidate = Candidate.query.get_or_404(candidate_id)

    db.session.delete(candidate)
    db.session.commit()