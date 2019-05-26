from flask import Blueprint, jsonify, request
from werkzeug import Response
from services.answer_service import AnswerService
from flask_api import status
from utils.response_formatter import response, response_text
from services.service_handler import ServiceHandler
from config.route_config import RouteConfig
from utils.validate_fields import *

route_name = RouteConfig.get('ANSWER_TYPE_NAME')
app_answer = Blueprint(route_name,__name__, url_prefix='/api')

def validate_answer_request(json):
    check_if_key_exists('text',json)
    check_empty_string(json['text'], 'text')           

@app_answer.route('/{}'.format(route_name), methods=['GET'])
def index():
    return Response('Hello {}'.format(route_name))

@app_answer.route(route_name, methods=['POST'])
def insert():
    try:
        json = request.get_json()

        validate_answer_request(json)

        obj = {
            "text": json['text']
        }

        ServiceHandler.get_service(route_name).insert(obj)    
        
        return response(status=status.HTTP_201_CREATED)

    except Exception as e:
        return response_text(str(e), status.HTTP_400_BAD_REQUEST)

@app_answer.route('/{}/<id>'.format(route_name), methods=['GET'])
def get(id):
    try:
        answer_obj = ServiceHandler.get_service(route_name).get(id)

        if not answer_obj:
            raise Exception('Object with id {} not found!'.format(id))

        return response(answer_obj.to_json(), status.HTTP_200_OK)

    except Exception as e:
        return response(str(e), status.HTTP_400_BAD_REQUEST)

@app_answer.route('/{}/<id>'.format(route_name), methods=['PUT'])
def update(id):
    try:
        json = request.get_json()

        validate_answer_request(json)

        obj = {
            "text" : json['text'],
            "id" : id
        }

        ServiceHandler.get_service(route_name).update(obj)

        return response(status=status.HTTP_200_OK)

    except Exception as e:
        return response(str(e), status.HTTP_400_BAD_REQUEST)

@app_answer.route('/{}/<id>'.format(route_name), methods=['DELETE'])
def delete(id):
    try:        
        ServiceHandler.get_service(route_name).delete(id)

        return response(status=status.HTTP_200_OK)
        
    except Exception as e:
        return response(str(e), status.HTTP_400_BAD_REQUEST)
