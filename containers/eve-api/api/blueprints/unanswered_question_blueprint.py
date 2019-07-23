from api.config.configuration import ROUTE_CONFIG
from flask import Blueprint, jsonify, request
from werkzeug import Response
from flask_api import status
from api.services.service_handler import ServiceHandler
from api.utils.validate_fields import check_empty_string, check_if_key_exists
from api.utils.response_formatter import response, response_text

route_name = ROUTE_CONFIG['UNANSWERED_QUESTION_TYPE_NAME']
app_unanswered_question = Blueprint(route_name,__name__, url_prefix='/api')

def validate_followup_request(json):
    keys = ['question']
    for k in keys:         
        check_if_key_exists(k, json)
        check_empty_string(k, json)

@app_unanswered_question.route(route_name, methods=['POST'])
def insert():
    try:
        json_obj = request.get_json()
        validate_followup_request(json_obj)
        
        obj = {
            "question": json_obj['question']            
        }
        ServiceHandler.get_service(route_name).insert(obj)
        return response(status=status.HTTP_201_CREATED)
    except Exception as e:
        return response_text(str(e), status.HTTP_400_BAD_REQUEST)
