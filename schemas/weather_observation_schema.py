from marshmallow import Schema, fields, post_load, post_dump

from models.weather_observation_model import WeatherObservation


class WeatherObservationSchema(Schema):
    id = fields.Integer(dump_only=True)
    datetime = fields.DateTime(dump_only=True, format='iso')
    city = fields.Str()
    text = fields.Str()

    @post_load
    def make_weather_observation(self, data, **kwargs):
        return WeatherObservation(**data)

    @post_dump
    def add_timezone_suffix(self, data, **kwargs):
        # Ugly workaround to localize UTC dates,
        # because datetime.utcnow.isoformat does not add the Z timezone suffix
        data['datetime'] = data['datetime'] + 'Z'

        return data
