import os

from flask import Flask
from flask_restful import Api

from api.v1.endpoint import Endpoint


def create_app():
    app = Flask(__name__)

    api = Api(app)
    api.add_resource(Endpoint, '/v1/endpoint')

    return app
