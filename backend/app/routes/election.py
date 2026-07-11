from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from app.middleware.role_required import role_required
from app.schemas.election_schema import election_schema
from app.services.election_service import (
    create_election,
    get_all_elections,
    get_election,
    update_election,
    delete_election
)

election_bp = Blueprint(
    "elections",
    __name__,
    url_prefix="/api/elections"
)


@election_bp.post("")
@role_required("Administrator")
def add_election():

    try:
        data = election_schema.load(
            request.get_json()
        )

    except ValidationError as err:
        return jsonify(err.messages), 400

    election = create_election(data)

    return jsonify({
        "message": "Election created successfully.",
        "election": {
            "id": election.election_id,
            "title": election.title,
            "status": election.status
        }
    })

@election_bp.get("")
@role_required("Administrator")
def list_elections():

    elections = get_all_elections()

    return jsonify([
        {
            "id": e.election_id,
            "title": e.title,
            "status": e.status
        }
        for e in elections
    ])
@election_bp.get("/<int:election_id>")
@role_required("Administrator")
def get_single_election(election_id):

    election = get_election(election_id)

    return jsonify({
        "id": election.election_id,
        "title": election.title,
        "description": election.description,
        "status": election.status
    })
@election_bp.put("/<int:election_id>")
@role_required("Administrator")
def edit_election(election_id):

    try:
        data = election_schema.load(request.get_json())

    except ValidationError as err:
        return jsonify(err.messages), 400

    election = update_election(election_id, data)

    return jsonify({
        "message": "Election updated successfully.",
        "election": {
            "id": election.election_id,
            "title": election.title
        }
    })
@election_bp.delete("/<int:election_id>")
@role_required("Administrator")
def remove_election(election_id):

    delete_election(election_id)

    return jsonify({
        "message": "Election deleted successfully."
    }),

