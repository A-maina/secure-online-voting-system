from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from app.middleware.role_required import role_required
from app.schemas.candidate_schema import candidate_schema
from app.services.candidate_service import (
    create_candidate,
    get_all_candidates,
    get_candidate,
    update_candidate,
    delete_candidate
)

candidate_bp = Blueprint(
    "candidates",
    __name__,
    url_prefix="/api/candidates"
)


@candidate_bp.post("")
@role_required("Administrator")
def add_candidate():

    try:
        data = candidate_schema.load(request.get_json())
    except ValidationError as err:
        return jsonify(err.messages), 400

    candidate = create_candidate(data)

    return jsonify({
        "message": "Candidate created successfully.",
        "candidate": {
            "id": candidate.candidate_id,
            "name": f"{candidate.first_name} {candidate.last_name}"
        }
    }), 201


@candidate_bp.get("")
@role_required("Administrator")
def list_candidates():

    candidates = get_all_candidates()

    return jsonify([
        {
            "id": c.candidate_id,
            "first_name": c.first_name,
            "last_name": c.last_name,
            "election_id": c.election_id
        }
        for c in candidates
    ])


@candidate_bp.get("/<int:candidate_id>")
@role_required("Administrator")
def get_single_candidate(candidate_id):

    candidate = get_candidate(candidate_id)

    return jsonify({
        "id": candidate.candidate_id,
        "first_name": candidate.first_name,
        "last_name": candidate.last_name,
        "manifesto": candidate.manifesto,
        "photo_url": candidate.photo_url,
        "election_id": candidate.election_id
    })


@candidate_bp.put("/<int:candidate_id>")
@role_required("Administrator")
def edit_candidate(candidate_id):

    try:
        data = candidate_schema.load(request.get_json())
    except ValidationError as err:
        return jsonify(err.messages), 400

    candidate = update_candidate(candidate_id, data)

    return jsonify({
        "message": "Candidate updated successfully.",
        "candidate": {
            "id": candidate.candidate_id,
            "name": f"{candidate.first_name} {candidate.last_name}"
        }
    })


@candidate_bp.delete("/<int:candidate_id>")
@role_required("Administrator")
def remove_candidate(candidate_id):

    delete_candidate(candidate_id)

    return jsonify({
        "message": "Candidate deleted successfully."
    })