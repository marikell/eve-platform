from flask import Flask, jsonify, abort, make_response, request
from flask_pymongo import PyMongo
from werkzeug import Response
from blueprints.entity_intent_answer_blueprint import app_entity_intent_answer
from blueprints.answer_blueprint import app_answer
from flask_api import FlaskAPI
import os

app = FlaskAPI(__name__)

port = 5001

def register_blueprints(app):
    app.register_blueprint(app_answer)
    app.register_blueprint(app_entity_intent_answer)

@app.route('/', methods=['GET'])
def get():
    return Response('Flask is running in port {}'.format(port))
    
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    register_blueprints(app)
    app.run(debug=True, host='0.0.0.0', port=port)