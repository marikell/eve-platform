from flask import Blueprint, request, jsonify
from werkzeug import Response
from flask_api import status
from utils import mongo_encoder as MongoEncoder
from utils.response_formatter import response, response_text
from services.service_handler import ServiceHandler
from config.route_config import RouteConfig

route_name = RouteConfig.get('ENTITY_INTENT_ANSWER_TYPE_NAME')
app_entity_intent_answer = Blueprint(route_name,__name__,url_prefix='/api')

@app_entity_intent_answer.route('/{}'.format(route_name), methods=['GET'])
def index():
    return Response('Hello {}'.format(route_name))

@app_entity_intent_answer.route(route_name, methods=['POST'])
def insert():
    try:
        json = request.get_json()
        entities = json['entities']
        intent = json['intent']
        answer = ServiceHandler.get_service(RouteConfig.get('ANSWER_TYPE_NAME')).get(json['answer_id']['$oid'])
        if answer is None:
            return response('Answer not found!', status.HTTP_400_BAD_REQUEST)

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
        entities = json['entities']
        intent = json['intent']
        
        action_answer = ServiceHandler.get_service(route_name).action_answer(entities, intent)
        
        if action_answer is not None:
            text = action_answer.answer_id.text

        return response_text(text)

    except:
       return response('')