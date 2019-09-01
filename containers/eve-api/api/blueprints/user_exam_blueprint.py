from api.config.configuration import ROUTE_CONFIG
from flask import Blueprint, jsonify, request
from werkzeug import Response
from flask_api import status
from api.services.service_handler import ServiceHandler
from api.utils.validate_fields import check_empty_string, check_if_key_exists
from api.utils.response_formatter import response, response_text
import json

route_name = ROUTE_CONFIG['USER_EXAM_TYPE_NAME']
app_user_exam = Blueprint(route_name,__name__, url_prefix='/api')

def validate_followup_request(json):
    keys = ['exam_id','user_id', 'exam_status']
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
            "user": user,
            "exam_status" : json_obj['exam_status']
        }
        
        inserted_id = ServiceHandler.get_service(route_name).insert(obj)
        obj = {
            'inserted_id': str(inserted_id)
        }

        return response(json.dumps(obj), status=status.HTTP_201_CREATED)
    except Exception as e:
        return response_text(str(e), status.HTTP_400_BAD_REQUEST)
    
@app_user_exam.route('/{}/<user_id>'.format(route_name), methods=['GET'])
def get_pending_exams_by_user(user_id):
    try:
        user = ServiceHandler.get_service(ROUTE_CONFIG['USER_TYPE_NAME']).get(user_id)

        if not user:
            raise Exception('User with id {} not found!'.format(user_id))

        obj = ServiceHandler.get_service(route_name).get_exam_status_by_user(user, 1)
        obj = obj.to_json() if obj else None

        return response(obj, status.HTTP_200_OK)
    except Exception as e:
        return response_text(str(e), status.HTTP_400_BAD_REQUEST)
    
@app_user_exam.route('/{}/<user_id>/<exam_id>'.format(route_name), methods=['GET'])
def get_user_exam(user_id, exam_id):
    try:
        user = ServiceHandler.get_service(ROUTE_CONFIG['USER_TYPE_NAME']).get(user_id)
        exam = ServiceHandler.get_service(ROUTE_CONFIG['EXAM_TYPE_NAME']).get(exam_id)

        if not user:
            raise Exception('User with id {} not found!'.format(user_id))
        
        if not exam:
            raise Exception('Exam with id {} not found!'.format(exam_id))

        obj = ServiceHandler.get_service(route_name).get_user_exam(user, exam)
        obj = obj.to_json() if obj else None

        return response(obj, status.HTTP_200_OK)
    except Exception as e:
        return response_text(str(e), status.HTTP_400_BAD_REQUEST)

@app_user_exam.route('/{}/<id>'.format(route_name), methods=['PUT'])
def update(id):
    try:        
        json_obj = request.get_json()

        obj = {
            'exam_status':json_obj['exam_status'],
            'id': id
        }
        ServiceHandler.get_service(route_name).update(obj)
        return response(status=status.HTTP_200_OK)
    except Exception as e:
        return response_text(str(e), status.HTTP_400_BAD_REQUEST)

@app_user_exam.route('/{}/<id>'.format(route_name), methods=['DELETE'])
def delete(id):
    try:        
        user = ServiceHandler.get_service(route_name).get(id)
        ServiceHandler.get_service(route_name).delete(id)
        return response(status=status.HTTP_200_OK)
        
    except Exception as e:
        return response(str(e), status.HTTP_400_BAD_REQUEST)
