from sqlalchemy.orm.session import Session

from api import db
from api import repositories
import abc

class Context():

    def __init__(self, session_factory = db.DefaultSessionFactory):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        self.userRepository = repositories.UserRepository(self.session)
        return self
    
    def __exit__(self, *args):
        self._rollback()
        self.session.close()

    def _commit(self):
        self.session.commit()

    def _rollback(self):
        self.session.rollback()
