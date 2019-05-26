from flask import Flask, jsonify, abort, make_response, request
from flask_pymongo import PyMongo
from werkzeug import Response
from blueprints.entity_intent_answer_blueprint import app_entity_intent_answer
from blueprints.answer_blueprint import app_answer
from services.service_handler import ServiceHandler
from flask_api import FlaskAPI
from utils.config_json import read_json
from mongoengine import connect
from config.route_config import RouteConfig
import os

flask_app = FlaskAPI(__name__)

def connect_db():
    config_object = read_json(os.path.abspath('./app/config/mongo_configuration.json'))

    connect(config_object['DATABASE_NAME'], host=config_object['DATABASE_URL'])

def register_blueprints(app):
    app.register_blueprint(app_answer)
    app.register_blueprint(app_entity_intent_answer)


@flask_app.route('/', methods=['GET'])
def get():
    return Response('Flask is running in port {}'.format(int(os.environ.get('PORT', 5001))))
    
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    connect_db()
    ServiceHandler.register_services()
    register_blueprints(flask_app)
    flask_app.run(debug=True, host='0.0.0.0', port=port)