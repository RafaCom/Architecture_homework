# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД
from flask import request

from app.dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        movies = self.session.query(Movie).all()
        return movies

    def get_one(self, mid):
        movie = self.session.query(Movie).get(mid)
        return movie

    def get_movies_by_filter(self):
        director_id = request.args.get('director_id')
        genres_id = request.args.get('genres_id')
        year = request.args.get('year')

        movies = self.session.query(Movie)

        if director_id:
            movies = movies.filter(Movie.id == director_id)
        if genres_id:
            movies = movies.filter(Movie.id == genres_id)
        if year:
            movies = movies.filter(Movie.year == year)

        movies = movies.all()

        return movies

    def create(self, data):
        movie = Movie(**data)

        self.session.add(movie)
        self.session.commit()

        return movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

        return movie

    def delete(self, mid):
        movie = self.get_one(mid)

        self.session.delete(movie)
        self.session.commit()

    