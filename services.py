from api import context
from api import security
from api.exceptions import ApplicationException
from api import model

class UserService():

    def login(self, context: context.Context, username, password):
        with context:
            user = context.userRepository.getByUsernamePassword(username, security.encrypt(password))
            if not user:
                raise ApplicationException('Credentials invalid.')        
        return model.create(username,username,security.generate_token(username),"admin")