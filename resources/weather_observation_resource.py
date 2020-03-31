from flask_restful import Resource, request
from flask_sqlalchemy import SQLAlchemy

from database.db import db
from schemas.weather_observation_schema import WeatherObservationSchema


class WeatherObservationResource(Resource):
    def post(self):
        json = request.get_json()
        new_observation = WeatherObservationSchema().load(json)

        db.session.add(new_observation)
        db.session.commit()

        return WeatherObservationSchema().dump(new_observation), 201
