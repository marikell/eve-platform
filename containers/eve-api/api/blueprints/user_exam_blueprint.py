from api.config.configuration import ROUTE_CONFIG
from flask import Blueprint, jsonify, request
from werkzeug import Response
from flask_api import status
from api.services.service_handler import ServiceHandler
from api.utils.validate_fields import check_empty_string, check_if_key_exists
from api.utils.response_formatter import response, response_text

route_name = ROUTE_CONFIG['USER_EXAM_TYPE_NAME']
app_user_exam = Blueprint(route_name,__name__, url_prefix='/api')

def validate_followup_request(json):
    keys = ['exam_id','user_id']
    for k in keys:         
        check_if_key_exists(k, json)
        check_empty_string(k, json)

@app_user_exam.route(route_name, methods=['POST'])
def insert():
    try:
        json_obj = request.get_json()
        validate_followup_request(json_obj)

        exam = ServiceHandler.get_service(ROUTE_CONFIG['EXAM_TYPE_NAME']).get(json_obj['exam_id'])

        if not exam:
            raise Exception('Exam not found!')

        user = ServiceHandler.get_service(ROUTE_CONFIG['USER_TYPE_NAME']).get(json_obj['user_id'])
        
        if not user:
            raise Exception('User not found!')
        
        obj = {
            "exam": exam,
            "user": user
        }
        ServiceHandler.get_service(route_name).insert(obj)
        return response(status=status.HTTP_201_CREATED)
    except Exception as e:
        return response_text(str(e), status.HTTP_400_BAD_REQUEST)
