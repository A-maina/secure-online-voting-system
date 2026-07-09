from marshmallow import Schema, fields, validate


class LoginSchema(Schema):

    email = fields.Email(
        required=True,
        validate=validate.Length(max=150)
    )

    password = fields.String(
        required=True,
        validate=validate.Length(min=8)
    )