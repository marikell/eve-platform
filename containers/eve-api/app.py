from flask import Flask, jsonify, abort, make_response, request
from flask_pymongo import PyMongo
from werkzeug import Response
from api.blueprints.entity_intent_answer_blueprint import  app_entity_intent_answer
from api.blueprints.exam_blueprint import app_exam
from api.blueprints.user_blueprint import app_user
from api.blueprints.answer_blueprint import app_answer
from api.blueprints.user_pregnancy_weeks_blueprint import app_usr_pregnancy_weeks
from api.blueprints.rasa_blueprint import app_rasa
from api.blueprints.fup_blueprint import app_fup
from api.services.service_handler import ServiceHandler
from flask_api import FlaskAPI
from mongoengine import connect
import os
from api.config.configuration import MONGO_CONFIG
from flask_mongoengine import MongoEngine
from api.models.db_model import db

flask_app = FlaskAPI(__name__)

flask_app.config['MONGODB_SETTINGS'] = {
    'db': MONGO_CONFIG['db'],
    'host': MONGO_CONFIG['host']
}

db.init_app(flask_app)

def register_blueprints(app):
    app.register_blueprint(app_answer)
    app.register_blueprint(app_entity_intent_answer)
    app.register_blueprint(app_user)
    app.register_blueprint(app_exam)
    app.register_blueprint(app_usr_pregnancy_weeks)
    app.register_blueprint(app_fup)
    app.register_blueprint(app_rasa)

@flask_app.route('/', methods=['GET'])
def get():
    return Response('Flask is running in port {}'.format(int(os.environ.get('PORT', 5001))))
    
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    ServiceHandler.register_services()
    register_blueprints(flask_app)
    flask_app.run(debug=True, host='0.0.0.0', port=port)