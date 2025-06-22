from marshmallow import Schema, fields, EXCLUDE

class WeatherItemSchema(Schema):
    description = fields.String(required=True)
    class Meta:
        unknown = EXCLUDE

class MainSchema(Schema):
    temp = fields.Float(required=True)
    humidity = fields.Integer(required=True)

    class Meta:
        unknown = EXCLUDE

class WindSchema(Schema):
    speed = fields.Float(required=True)

    class Meta:
        unknown = EXCLUDE

class WeatherSchema(Schema):
    weather = fields.List(fields.Nested(WeatherItemSchema), required=True)
    main = fields.Nested(MainSchema, required=True)
    wind = fields.Nested(WindSchema, required=True)
    name = fields.String(required=True)

    class Meta:
        unknown = EXCLUDE  # Ignores extra fields like "feels_like", "gust", etc.
