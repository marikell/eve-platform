from flask import Blueprint, jsonify, request
from werkzeug import Response
import json
from flask_api import status
from api.utils.response_formatter import response, response_text
from api.services.fup_service import get_users_exams
from api.services.service_handler import ServiceHandler
from api.config.configuration import ROUTE_CONFIG
from api.utils.validate_fields import check_empty_string, check_empty_string_in_array, check_if_key_exists
from api.enums.user_enums import UserTypeEnum

route_name = ROUTE_CONFIG['USER_TRIMESTER_TYPE_NAME']
app_usr_trimester = Blueprint(route_name,__name__, url_prefix='/api')

@app_usr_trimester.route('/{}/<user_id>'.format(route_name), methods=['GET'])
def get_user_trimester(user_id):
    try:
        user = ServiceHandler.get_service(ROUTE_CONFIG['USER_TYPE_NAME']).get(user_id)

        if not user:
            raise Exception('User with id {} not found!'.format(user_id))

        obj = ServiceHandler.get_service(route_name).get_by_user_id(user.id)

        if obj.user_id['user_type'] != UserTypeEnum.pregnant.value:
            raise Exception('This user is not pregnant to control user_pregnancy_days records')

        return response(obj.to_json(), status.HTTP_200_OK)
    except Exception as e:
        return response_text(str(e), status.HTTP_400_BAD_REQUEST)       

@app_usr_trimester.route(route_name, methods=['POST'])
def insert():
    try:        
        json_obj = request.get_json()

        check_if_key_exists('trimester', json_obj)
        check_if_key_exists('start_date', json_obj)
        check_if_key_exists('user_id', json_obj)

        user_id = json_obj['user_id']

        user = ServiceHandler.get_service(ROUTE_CONFIG['USER_TYPE_NAME']).get(user_id)

        if not user:
            raise Exception('User with id {} not found!'.format(user_id))

        tri_obj = {
            'trimester':json_obj['trimester'],
            'start_date':json_obj['start_date'],
            'user' : user
        }

        ServiceHandler.get_service(route_name).insert(tri_obj)

        return response(status=status.HTTP_200_OK)

    except Exception as e:
        return response_text(str(e), status.HTTP_400_BAD_REQUEST)

@app_usr_trimester.route('/{}/<id>'.format(route_name), methods=['PUT'])
def update(id):
    try:        
        json_obj = request.get_json()

        check_if_key_exists('trimester', json_obj)

        days_obj = {
            'trimester':json_obj['trimester'],
            'id' : id
        }

        ServiceHandler.get_service(route_name).update(days_obj)

        return response(status=status.HTTP_200_OK)

    except Exception as e:
        return response_text(str(e), status.HTTP_400_BAD_REQUEST)