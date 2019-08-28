from flask import Flask, jsonify, abort, make_response, request
from flask_pymongo import PyMongo
from werkzeug import Response
from api.blueprints.entity_intent_answer_blueprint import  app_entity_intent_answer
from api.blueprints.exam_blueprint import app_exam
from api.blueprints.user_blueprint import app_user
from api.blueprints.tip_blueprint import app_tip
from api.blueprints.answer_blueprint import app_answer
from api.blueprints.rasa_blueprint import app_rasa
from api.blueprints.fup_blueprint import app_fup
from api.blueprints.user_exam_blueprint import app_user_exam
from api.blueprints.unanswered_question_blueprint import app_unanswered_question
from api.blueprints.user_trimester_blueprint import app_usr_trimester
from api.blueprints.form_blueprint import app_form
from api.blueprints.notification_user_blueprint import app_notification_user
from api.blueprints.notify_blueprint import app_notify
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
    app.register_blueprint(app_fup)
    app.register_blueprint(app_rasa)
    app.register_blueprint(app_unanswered_question)
    app.register_blueprint(app_usr_trimester)
    app.register_blueprint(app_form)
    app.register_blueprint(app_tip)
    app.register_blueprint(app_notify)
    app.register_blueprint(app_notification_user)
    # app.register_blueprint(app_user_exam)

@flask_app.route('/', methods=['GET'])
def get():
    return Response('Flask is running in port {}'.format(int(os.environ.get('PORT', 5001))))
    
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    ServiceHandler.register_services()
    register_blueprints(flask_app)
    flask_app.run(debug=True, host='0.0.0.0', port=port)