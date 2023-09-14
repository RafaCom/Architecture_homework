from app.dao.director import DirectorDAO


class DirectorService:

    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def get_directors(self):
        return self.director_dao.get_all()

    def get_one(self, did):
        return self.director_dao.get_one(did)

