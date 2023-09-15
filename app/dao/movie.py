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

    def get_by_director(self, did):
        movie = self.session.query(Movie).filter(Movie.director_id == did).all()
        return movie

    def get_by_genre(self, gid):
        movie = self.session.query(Movie).filter(Movie.genre_id == gid).all()
        return movie

    def get_by_year(self, year):
        movie = self.session.query(Movie).filter(Movie.year == year).all()
        return movie

    def create(self, data):
        movie = Movie(**data)

        self.session.add(movie)
        self.session.commit()

        return movie.id

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

        return movie

    def delete(self, mid):
        movie = self.get_one(mid)

        self.session.delete(movie)
        self.session.commit()

    