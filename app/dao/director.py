from app.dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        directors = self.session.query(Director).all()
        return directors

    def get_one(self, did):
        director = self.session.query(Director).get(did)
        return director
