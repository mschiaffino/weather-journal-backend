from flask import Flask
from flask_restful import Api

application = Flask(__name__)
api = Api(application)

if __name__ == '__main__':
    application.run()
