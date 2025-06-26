from marshmallow import Schema, fields,EXCLUDE


class JokeSchema(Schema):
    type = fields.String(required=True)
    setup = fields.String(required=True)
    punchline = fields.String(required=True)
    id = fields.Integer(required=True)

    class Meta:
        unknown = EXCLUDE  # Ignore extra fields if present