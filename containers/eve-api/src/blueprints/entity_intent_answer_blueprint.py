from flask import Blueprint, request, jsonify
from werkzeug import Response
from utils import mongo_encoder as MongoEncoder
from utils.request_result import RequestResult
from enums.status_code_enum import StatusCode
from services.entity_intent_answer_service import EntityIntentAnswerService
from services.answer_service import AnswerService

route_name = 'entity-intent-answer'
app_entity_intent_answer = Blueprint(route_name,__name__)

#services
entity_intent_answer_service = EntityIntentAnswerService()
answer_service = AnswerService()

@app_entity_intent_answer.route('/{}'.format(route_name), methods=['GET'])
def index():
    return Response('Hello {}'.format(route_name))

@app_entity_intent_answer.route('/api/{}'.format(route_name), methods=['POST'])
def insert():
    try:
        json = request.get_json()
        entities = json['entities']
        intent = json['intent']
        answer = answer_service.get(json['answer_id']['$oid'])

        if answer is None:
            return RequestResult.response(StatusCode.OK, False, 'Answer not found!')

        obj = {
            'entities': entities,
            'intent': intent,
            'answer': answer
        }

        entity_intent_answer_service.insert(obj)
        return RequestResult.response(StatusCode.CREATED, True)

    except Exception as e:
        return RequestResult.response(StatusCode.OK, False, str(e))

@app_entity_intent_answer.route('/api/action-answer', methods=['POST'])
def findby_intent_entities():
    try:
        json = request.get_json()
        entities = json['entities']
        intent = json['intent']
        
        action_answer = entity_intent_answer_service.action_answer(entities, intent)
        
        if action_answer is not None:
            text = action_answer.answer_id.text

        return RequestResult.response_content(text)

    except:
       return RequestResult.response_content('')