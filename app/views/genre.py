from flask_restx import Resource, Namespace

from app.dao.model.genre import GenreSchema
from container import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = genre_service.get_genres()
        result = GenreSchema(many=True).dump(genres)
        return result, 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid: int):
        genre = genre_service.get_one(gid)
        result = GenreSchema().dump(genre)
        return result, 200


