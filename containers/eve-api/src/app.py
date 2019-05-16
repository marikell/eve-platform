from flask import Flask, jsonify, abort, make_response, request
from flask_pymongo import PyMongo
from werkzeug import Response
from blueprints.entity_intent_answer_blueprint import app_entity_intent_answer
from blueprints.answer_blueprint import app_answer

app = Flask(__name__)

def register_blueprints(app):
    app.register_blueprint(app_answer)
    app.register_blueprint(app_entity_intent_answer)

@app.route('/', methods=['GET'])
def get():
    return Response('Flask is running in port 5001')
    
if __name__ == '__main__':
    register_blueprints(app)
    app.run(debug=True, host='0.0.0.0', port='5001')