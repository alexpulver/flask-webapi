from flask_restful import Resource


class Endpoint(Resource):

    def get(self):
        return 'Got get', 200

    def post(self):
        return 'Got post', 201
