from app.extensions import db
from app.models.election import Election


def create_election(data):
    election = Election(
        title=data["title"],
        description=data.get("description"),
        start_date=data["start_date"],
        end_date=data["end_date"]
    )

    db.session.add(election)
    db.session.commit()

    return election


def get_all_elections():
    return Election.query.order_by(
        Election.election_id.desc()
    ).all()


def get_election(election_id):
    return Election.query.get_or_404(election_id)


def update_election(election_id, data):
    election = Election.query.get_or_404(election_id)

    election.title = data["title"]
    election.description = data.get("description")
    election.start_date = data["start_date"]
    election.end_date = data["end_date"]

    db.session.commit()

    return election


def delete_election(election_id):
    election = Election.query.get_or_404(election_id)

    db.session.delete(election)
    db.session.commit()