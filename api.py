# from app import app
from app import *
from flask import jsonify
from flask.ext.restful import Api, Resource
from marshmallow import Schema, fields, ValidationError

api = Api(app)

# SCHEMAS


class SignalSchema(Schema):

    class Meta:
        fields = ('id', 'time_of_creation', 'opening_time', 'closing_time', 'symbol_id')


class SignalsResource(Resource):

    def get(self):

        signals = Signal.query.all()
        serializer = SignalSchema(many=True)
        result = serializer.dump(signals)
        return jsonify({"signals": result.data})

api.add_resource(SignalsResource, '/api')