from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from resources.cities_resource import CitiesResource

application = Flask(__name__)
api = Api(application)
CORS(application)

api.add_resource(CitiesResource, '/cities')

if __name__ == '__main__':
    application.run(debug=True)
