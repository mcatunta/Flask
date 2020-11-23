from sqlalchemy.orm import session
from api import entities

class UserRepository():
    def __init__(self, session):
        self.session = session

    def create(self, user):
        self.session.add(user)

    def getByUsernamePassword(self, username, password):
        return self.session.query(entities.User).filter_by(username=username, password=password).first()