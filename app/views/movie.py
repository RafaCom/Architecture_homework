# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service
from flask import request
from flask_restx import Resource, Namespace

from app.dao.model.movie import MovieSchema
from container import movie_service

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        movies = movie_service.get_movies()
        return movies_schema.dump(movies), 200

    def post(self):
        req_json = request.json

        movie_service.create(req_json)

        return f"Фильм --- {req_json.get('title')} --- добавлен", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid: int):
        try:
            movie = movie_service.get_one(mid)
            return movie_schema.dump(movie), 200
        except Exception as e:
            return str(e), 404

    def put(self, mid: int):
        req_json = request.json
        req_json['id'] = mid

        movie_service.update(req_json)

        return "", 204
    # Данные фильма --- {req_json.get('title')} --- полностью обновлены   |||  код 204 ничего не возвращает (204 NO CONTENT)

    def patch(self, mid: int):
        req_json = request.json
        req_json['id'] = mid

        movie_service.update_partial(req_json)

        return "", 204

    def delete(self, mid: int):
        movie_service.delete(mid)

        return f"Фильм с ID --- {mid} --- УДАЛЕН", 204

