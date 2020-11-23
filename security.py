import hashlib
import jwt
import datetime
from functools import wraps
from flask import request

from api import config
from api.exceptions import AuthorizeException

def encrypt(word:str):
    encrypted = hashlib.md5(word.encode())
    return encrypted.hexdigest()

def generate_token(user_id):
    timestamp = datetime.datetime.utcnow()
    payload = {
        'exp': timestamp + datetime.timedelta(seconds=config.get_jwt_lifetime_seconds()),
        'iat': timestamp,        
        'sub': user_id
    }
    token = jwt.encode(payload, config.get_jwt_secret(), algorithm='HS256')    
    return token.decode("utf-8")

def get_user_of_token(token):
    payload = jwt.decode(token, config.get_jwt_secret())
    return payload['sub']

def get_authorizations():
    return {
        'apikey': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'authorization'
        }
    }

def authorize(f):
    @wraps(f)
    def  decorated_function(self,*args, **kws):
        if not 'Authorization' in request.headers:
            raise AuthorizeException('Not has authorization')        
        data = request.headers.get('Authorization')
        token = str.replace(str(data), 'Bearer ','')
        try:
            user = jwt.decode(token, config.get_jwt_secret(), algorithms=['HS256'])['sub']
        except Exception as e:
            print(str(e))
            raise AuthorizeException('Invalid token')
        
        return f(self,user, *args, **kws)
    return decorated_function