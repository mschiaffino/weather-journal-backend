from marshmallow import Schema


class WeatherObservationSchema(Schema):
    id = fields.Integer(dump_only=True)
    datetime = fields.DateTime(dump_only=True, format='iso')
    city = fields.Str()
    text = fields.Str()
