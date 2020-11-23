from flask_restful_swagger_3 import swagger, Resource
from flask_restful.reqparse import RequestParser
from flask import jsonify, request

from api import context
from api import services
from api.model import LoggedInModel
from api import security

context = context.Context()

login_parser = RequestParser()
login_parser.add_argument('username', type=str, required=True)
login_parser.add_argument('password', type=str, required=True)


class UserLogin(Resource):
    @swagger.tags(['user'])
    @swagger.reqparser(name='LoggedIn', parser=login_parser)
    @swagger.reorder_with(LoggedInModel, description='Result logged in')
    def post(self):
        arg = login_parser.parse_args()
        userService = services.UserService()
        return userService.login(context, arg.get('username'), arg.get('password'))

    @swagger.tags(['user'])
    @security.authorize
    @swagger.reorder_with(LoggedInModel, description='Result logged in')
    def get(self,user):
        userService = services.UserService()
        return userService.login(context, 'admin', 'admin')

