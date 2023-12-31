# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.

from app.dao.movie import MovieDAO


class MovieService:

    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_movies(self):
        return self.movie_dao.get_all()

    def get_one(self, mid):
        return self.movie_dao.get_one(mid)

    def get_by_director(self, did):
        return self.movie_dao.get_by_director(did)

    def get_by_genre(self, gid):
        return self.movie_dao.get_by_genre(gid)

    def get_by_year(self, year):
        return self.movie_dao.get_by_year(year)

    def create(self, data):
        return self.movie_dao.create(data)

    def update(self, data):
        mid = data.get('id')

        movie = self.get_one(mid)

        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        movie.genre_id = data.get('genre_id')
        movie.director_id = data.get('director')

        return self.movie_dao.update(movie)

    def update_partial(self, data):
        mid = data.get('id')

        movie = self.get_one(mid)

        if 'title' in data:
            movie.title = data.get('title')
        if 'description' in data:
            movie.description = data.get('description')
        if 'trailer' in data:
            movie.trailer = data.get('trailer')
        if 'year' in data:
            movie.year = data.get('year')
        if 'rating' in data:
            movie.rating = data.get('rating')
        if 'genre_id' in data:
            movie.genre_id = data.get('genre_id')
        if 'director' in data:
            movie.director_id = data.get('director')

        self.movie_dao.update(movie)

    def movies_by_filter(self):
        return self.movie_dao.get_movies_by_filter()

    def delete(self, mid):
        self.movie_dao.delete(mid)
