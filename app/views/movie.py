# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service
from flask import request, jsonify
from flask_restx import Resource, Namespace

from app.dao.model.movie import MovieSchema
from container import movie_service

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        movies = movie_service.get_movies()
        result = MovieSchema(many=True).dump(movies)
        return result, 200

    def post(self):
        req_json = request.json

        movie_id = movie_service.create(req_json)

        response = jsonify()
        response.status_code = 201
        response.headers['location'] = f'/{movie_id}'
        response.data = f'Фильм --- {req_json.get("title")} --- ДОБАВЛЕН'

        return response


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid: int):
        try:
            movie = movie_service.get_one(mid)
            result = MovieSchema().dump(movie)
            return result, 200
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

