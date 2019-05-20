from flask import Blueprint, request, jsonify
from werkzeug import Response
from flask_api import status
from utils import mongo_encoder as MongoEncoder
from utils.response_formatter import response
from services.entity_intent_answer_service import EntityIntentAnswerService
from services.answer_service import AnswerService

route_name = 'entity-intent-answer'
app_entity_intent_answer = Blueprint(route_name,__name__,url_prefix='/api')

#services
entity_intent_answer_service = EntityIntentAnswerService()
answer_service = AnswerService()

@app_entity_intent_answer.route('/{}'.format(route_name), methods=['GET'])
def index():
    return Response('Hello {}'.format(route_name))

@app_entity_intent_answer.route(route_name, methods=['POST'])
def insert():
    try:
        json = request.get_json()
        entities = json['entities']
        intent = json['intent']
        answer = answer_service.get(json['answer_id']['$oid'])

        if answer is None:
            return response('Answer not found!', status.HTTP_400_BAD_REQUEST)

        obj = {
            'entities': entities,
            'intent': intent,
            'answer': answer
        }

        entity_intent_answer_service.insert(obj)
        return response(status=status.HTTP_201_CREATED)

    except Exception as e:
        return response(str(e), status.HTTP_400_BAD_REQUEST)

@app_entity_intent_answer.route('action-answer', methods=['POST'])
def findby_intent_entities():
    try:
        json = request.get_json()
        entities = json['entities']
        intent = json['intent']
        
        action_answer = entity_intent_answer_service.action_answer(entities, intent)
        
        if action_answer is not None:
            text = action_answer.answer_id.text

        return response(text)

    except:
       return response('')