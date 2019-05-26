from flask import Blueprint, request, jsonify
from werkzeug import Response
from flask_api import status
from utils.response_formatter import response, response_text
from services.service_handler import ServiceHandler
from config.route_config import RouteConfig
from utils.validate_fields import *

route_name = RouteConfig.get('ENTITY_INTENT_ANSWER_TYPE_NAME')
app_entity_intent_answer = Blueprint(route_name,__name__,url_prefix='/api')

def validate_entity_intent_request(json):
    
    keys = ['entities', 'intent']

    for k in keys:
        check_if_key_exists(k, json)

    check_empty_string(json['intent'], 'intent')

    if len(json['entities']) == 0:
        raise Exception('Not allowed empty array of entities')

    check_empty_string_in_array(json['entities'], 'entities')


@app_entity_intent_answer.route('/{}'.format(route_name), methods=['GET'])
def index():
    return Response('Hello {}'.format(route_name))

@app_entity_intent_answer.route(route_name, methods=['POST'])
def insert():
    try:
        json = request.get_json()

        answer = ServiceHandler.get_service(RouteConfig.get('ANSWER_TYPE_NAME')).get(json['answer_id']['$oid'])

        if not answer:
            raise Exception('Answer not found!')

        validate_entity_intent_request(json)
        
        intent = json['intent']
        entities = json['entities']
        
        obj = {
            'entities': entities,
            'intent': intent,
            'answer': answer
        }

        ServiceHandler.get_service(route_name).insert(obj)

        return response(status=status.HTTP_201_CREATED)

    except Exception as e:
        return response(str(e), status.HTTP_400_BAD_REQUEST)

@app_entity_intent_answer.route('action-answer', methods=['POST'])
def findby_intent_entities():
    try:
        json = request.get_json()

        validate_entity_intent_request(json)
        
        entities = json['entities']
        intent = json['intent']
        
        action_answer = ServiceHandler.get_service(route_name).getby_intent_entities(entities, intent)
        
        if action_answer:
            text = action_answer.answer_id.text

        return response_text(text)

    except:
       return response('')

@app_entity_intent_answer.route('/{}/<id>'.format(route_name), methods=['GET'])
def get(id):
    try:
        entity_intent_answer_obj = ServiceHandler.get_service(route_name).get(id)

        return response(entity_intent_answer_obj.to_json(), status.HTTP_200_OK)

    except Exception as e:
        return response(str(e), status.HTTP_400_BAD_REQUEST)

@app_entity_intent_answer.route('/{}/<id>'.format(route_name), methods=['DELETE'])
def delete(id):
    try:        
        ServiceHandler.get_service(route_name).delete(id)

        return response(status=status.HTTP_200_OK)
        
    except Exception as e:
        return response(str(e), status.HTTP_400_BAD_REQUEST)

@app_entity_intent_answer.route('/{}/<id>'.format(route_name), methods=['PUT'])
def update(id):
    try:
        json = request.get_json()
        
        answer = ServiceHandler.get_service(RouteConfig.get('ANSWER_TYPE_NAME')).get(json['answer_id']['$oid'])

        if not answer:
            raise Exception('Answer not found!')

        validate_entity_intent_request(json)

        intent = json['intent']
        entities = json['entities']        

        obj = {
            'entities': entities,
            'intent': intent,
            'answer': answer,
            'id': id
        }

        ServiceHandler.get_service(route_name).update(obj)

        return response(status=status.HTTP_200_OK)

    except Exception as e:
        return response(str(e), status.HTTP_400_BAD_REQUEST)