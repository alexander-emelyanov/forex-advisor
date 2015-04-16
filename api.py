from app import app
from flask.ext.restful import Api, Resource

api = Api(app)


class RecentSignals(Resource):

    def get(self):
        return {'hello': 'world'}

api.add_resource(RecentSignals, '/api')