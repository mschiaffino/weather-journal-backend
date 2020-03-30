from marshmallow import Schema, fields


class CitySchema(Schema):
    name = fields.Str()
    wind = fields.Str()
