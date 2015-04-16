# from app import app
from app import *
from flask import jsonify
from flask.ext.restful import Api, Resource
from marshmallow import Schema, fields, ValidationError

api = Api(app)

# SCHEMAS


class SimpleDictionarySchema(Schema):

    class Meta:
        fields = ('id', 'code', 'name')


class SignalSchema(Schema):

    symbol = fields.Nested(SimpleDictionarySchema)
    direction = fields.Nested(SimpleDictionarySchema)
    duration = fields.Nested(SimpleDictionarySchema)
    predictor = fields.Nested(SimpleDictionarySchema)

    class Meta:
        fields = ('id', 'time_of_creation', 'opening_time', 'closing_time', 'symbol', 'direction', 'duration',
                  'predictor')


# RESOURCES
class SymbolResource(Resource):

    def get(self):
        symbols = Symbol.query.all()
        serializer = SimpleDictionarySchema(many=True)
        result = serializer.dump(symbols)
        return jsonify({"symbols": result.data})


class SignalsResource(Resource):

    def get(self):

        signals = Signal.query.all()
        serializer = SignalSchema(many=True)
        result = serializer.dump(signals)
        return jsonify({"signals": result.data})

api.add_resource(SymbolResource, '/api/symbols')
api.add_resource(SignalsResource, '/api/signals')