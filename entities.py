from api import db
from sqlalchemy import Column, Integer, Float, String

class User(db.Base):
    __tablename__ = 'user'
    id_user = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f'User {self.username}'

    def __str__(self):
        return self.username