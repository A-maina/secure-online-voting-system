from marshmallow import Schema, fields, validate


class ElectionSchema(Schema):
    title = fields.String(
        required=True,
        validate=validate.Length(min=5, max=150)
    )

    description = fields.String(required=False)

    start_date = fields.DateTime(
        required=True,
        format="%Y-%m-%d %H:%M:%S"
    )

    end_date = fields.DateTime(
        required=True,
        format="%Y-%m-%d %H:%M:%S"
    )


election_schema = ElectionSchema()