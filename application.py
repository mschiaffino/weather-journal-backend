import os

from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from resources.cities_resource import CitiesResource

application = Flask(__name__)
api = Api(application)
CORS(application)

SQLITE_FILE_PATH = f'{os.path.abspath(os.path.dirname(__file__))}/db/wj.db'
application.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:////{SQLITE_FILE_PATH}'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api.add_resource(CitiesResource, '/cities')

if __name__ == '__main__':
    application.run(debug=True)
