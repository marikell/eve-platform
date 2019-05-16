from flask import Blueprint, jsonify, request
from werkzeug import Response
from utils import mongo_encoder as MongoEncoder
from services.answer_service import AnswerService
from utils.request_result import RequestResult
from enums.status_code_enum import StatusCode

route_name = 'answer'
app_answer = Blueprint(route_name,__name__, url_prefix='/api')

#service
answer_service = AnswerService()

@app_answer.route('/{}'.format(route_name), methods=['GET'])
def index():
    return Response('Hello {}'.format(route_name))

@app_answer.route(route_name, methods=['POST'])
def insert():
    try:
        json = request.get_json()
        text = json['text']

        if text is None:
            return RequestResult.response(StatusCode.OK, False, 'Not allowed empty string!')

        obj = {
            "text": text
        }

        answer_service.insert(obj)    
        return RequestResult.response(StatusCode.CREATED, True)
    except Exception as e:
        return RequestResult.response(StatusCode.OK, False, str(e))

@app_answer.route('/{}/<id>'.format(route_name), methods=['GET'])
def get(id):
    try:
        answer_obj = answer_service.get(id)

        return RequestResult.response_content(answer_obj.to_json())

    except Exception as e:
        return RequestResult.response(StatusCode.OK, False, str(e))