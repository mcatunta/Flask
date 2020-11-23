from flask_restful_swagger_3 import Schema

def create(name, username, token, rol):
    return {"names": name, "username": username, "token": token, "rol": rol}

class LoggedInModel(Schema):
    type = 'object'
    properties = {
        "name": {'type':'string'},
        "username": {'type':'string'},
        "token": {'type':'string'},
        "rol": {'type':'string'}
    }
    