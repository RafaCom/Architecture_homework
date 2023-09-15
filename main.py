# основной файл приложения. здесь конфигурируется фласк, сервисы, SQLAlchemy и все остальное что требуется для приложения.
# этот файл часто является точкой входа в приложение
import sqlite3

from flask import Flask
from flask_restx import Api

from app.config import Config
from app.dao.model.director import Director
from app.dao.model.genre import Genre
from app.dao.model.movie import Movie
# from models import Review, Book
from app.database import db
from app.views.movie import movie_ns
from app.views.genre import genre_ns
from app.views.director import director_ns


# функция создания основного объекта app
def create_app(config_object):
    application = Flask(__name__)
    application.app_context().push()
    application.config.from_object(config_object)
    register_extensions(application)
    return application


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)
    create_data(application)


# подключение к БД
def database_connection(q):
    with sqlite3.connect('movies.db') as conn:
        cursor = conn.cursor()
        query = cursor.execute(q)
        result = query.fetchall()
    return result


# функция
def create_data(application):
    with application.app_context():
        db.drop_all()
        db.create_all()

    movies = database_connection(""" SELECT * FROM movie """)

    all_movies = []
    for movie in movies:
        new_movie = Movie(
            id=movie[0],
            title=movie[1],
            description=movie[2],
            trailer=movie[3],
            year=movie[4],
            rating=movie[5],
            genre_id=movie[6],
            director_id=movie[7]

        )
        all_movies.append(new_movie)
    # print(all_movies)

    with db.session.begin():
        db.session.add_all(all_movies)

    genres = database_connection(""" SELECT * FROM genre """)
    all_genres = []
    for genre in genres:
        new_genre = Genre(
            id=genre[0],
            name=genre[1]
        )
        all_genres.append(new_genre)
    # print(all_genres)

    with db.session.begin():
        db.session.add_all(all_genres)

    directors = database_connection(""" SELECT * FROM director """)
    all_directors = []
    for director in directors:
        new_director = Director(
            id=director[0],
            name=director[1]
        )
        all_directors.append(new_director)

    with db.session.begin():
        db.session.add_all(all_directors)


if __name__ == '__main__':
    config = Config()
    app = create_app(config)
    app.run(host=config.HOST, port=config.PORT)
