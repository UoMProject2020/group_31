import CouchDBViews as view
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask import jsonify

app = Flask(__name__)
api = Api(app)


class Voters(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('city', required=True)
        args = parser.parse_args()
        result = view.create_views_voter("votersdata", args['city'])
        return jsonify(result)

api.add_resource(Voters, '/voters')

if __name__ == '__main__':
    app.run(debug=True)



