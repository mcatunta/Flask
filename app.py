from flask import Flask, request, jsonify
from flask_restful_swagger_3 import Api, get_swagger_blueprint
from flask_cors import CORS

from api import entrypoints
from api import handlerexception

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(entrypoints.UserLogin, '/api/user/login')

handlerexception.register_error_handler(app)

servers = [{"url": "http://localhost:5000"}]
swagger_blueprint = get_swagger_blueprint(
    api.open_api_json,
    swagger_prefix_url='/api/doc',
    swagger_url='swagger.json',
    title='Example', version='1', servers=servers)

app.register_blueprint(swagger_blueprint)
        
app.run(debug=True)