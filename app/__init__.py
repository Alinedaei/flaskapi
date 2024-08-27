from flask import Flask
from flask_restful import Api
from app.api import MyResource

def create_app():
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(MyResource, '/myendpoint')
    return app

