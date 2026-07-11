from marshmallow import Schema, fields, validate


class CandidateSchema(Schema):
    election_id = fields.Integer(required=True)

    first_name = fields.String(
        required=True,
        validate=validate.Length(min=2, max=100)
    )

    last_name = fields.String(
        required=True,
        validate=validate.Length(min=2, max=100)
    )

    manifesto = fields.String(required=False)

    photo_url = fields.String(required=False)


candidate_schema = CandidateSchema()