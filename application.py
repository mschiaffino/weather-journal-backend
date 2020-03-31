import os

from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from database.db import db

from resources.cities_resource import CitiesResource
from resources.weather_observation_resource import WeatherObservationResource

SQLITE_FILE_PATH = (f'{os.path.abspath(os.path.dirname(__file__))}'
                    f'/database/wj.db')


def create_app():
    application = Flask(__name__)
    application.config['SQLALCHEMY_DATABASE_URI'] = (
        f'sqlite:////{SQLITE_FILE_PATH}')
    application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    CORS(application)

    db.init_app(application)

    api = Api(application)
    api.add_resource(CitiesResource, '/cities')
    api.add_resource(WeatherObservationResource, '/observations')

    return application


def setup_database(application):
    with application.app_context():
        db.create_all()


def db_file_exists():
    return os.path.isfile(SQLITE_FILE_PATH)


if __name__ == '__main__':
    application = create_app()

    if not db_file_exists():
        setup_database(application)

    application.run(debug=True)
