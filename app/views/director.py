from flask_restx import Resource, Namespace

from app.dao.model.director import DirectorSchema
from container import director_service

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = director_service.get_directors()
        return directors_schema.dump(directors), 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did: int):
        director = director_service.get_one(did)
        return director_schema.dump(director), 200
