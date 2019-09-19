from flask import Blueprint, request, jsonify
from werkzeug import Response
from flask_api import status
from api.utils.response_formatter import response, response_text
from api.services.service_handler import ServiceHandler
from api.config.configuration import ROUTE_CONFIG
from api.utils.validate_fields import *

route_name = ROUTE_CONFIG['INTENT_ANSWER_TYPE_NAME']
app_intent_answer = Blueprint(route_name,__name__,url_prefix='/api')

def validate_intent_request(json):
    
    keys = ['intent']

    for k in keys:
        check_if_key_exists(k, json)

    check_empty_string(json['intent'], 'intent')

@app_intent_answer.route('/{}'.format(route_name), methods=['GET'])
def index():
    return Response('Hello {}'.format(route_name))

@app_intent_answer.route(route_name, methods=['POST'])
def insert():
    try:
        json = request.get_json()

        answer = ServiceHandler.get_service(ROUTE_CONFIG['ANSWER_TYPE_NAME']).get(json['answer_id']['$oid'])

        if not answer:
            raise Exception('Answer not found!')

        validate_intent_request(json)
        
        intent = json['intent']
        
        obj = {
            'intent': intent,
            'answer': answer
        }

        ServiceHandler.get_service(route_name).insert(obj)

        return response(status=status.HTTP_201_CREATED)

    except Exception as e:
        return response(str(e), status.HTTP_400_BAD_REQUEST)

@app_intent_answer.route('action-answer', methods=['POST'])
def findby_intent_entities():
    try:
        json = request.get_json()

        validate_intent_request(json)
        
        intent = json['intent']
        
        action_answer = ServiceHandler.get_service(route_name).get_by_intent(intent)
        
        if action_answer:
            text = action_answer.answer_id.text

        return response_text(text)

    except:
       return response('')

@app_intent_answer.route('/{}/<id>'.format(route_name), methods=['GET'])
def get(id):
    try:
        intent_answer_obj = ServiceHandler.get_service(route_name).get(id)

        return response(intent_answer_obj.to_json(), status.HTTP_200_OK)

    except Exception as e:
        return response(str(e), status.HTTP_400_BAD_REQUEST)

@app_intent_answer.route('/{}/<id>'.format(route_name), methods=['DELETE'])
def delete(id):
    try:        
        ServiceHandler.get_service(route_name).delete(id)

        return response(status=status.HTTP_200_OK)
        
    except Exception as e:
        return response(str(e), status.HTTP_400_BAD_REQUEST)

@app_intent_answer.route('/{}/<id>'.format(route_name), methods=['PUT'])
def update(id):
    try:
        json = request.get_json()
        
        answer = ServiceHandler.get_service(ROUTE_CONFIG['ANSWER_TYPE_NAME']).get(json['answer_id']['$oid'])

        if not answer:
            raise Exception('Answer not found!')

        validate_intent_request(json)

        intent = json['intent']

        obj = {
            'intent': intent,
            'answer': answer,
            'id': id
        }

        ServiceHandler.get_service(route_name).update(obj)

        return response(status=status.HTTP_200_OK)

    except Exception as e:
        return response(str(e), status.HTTP_400_BAD_REQUEST)