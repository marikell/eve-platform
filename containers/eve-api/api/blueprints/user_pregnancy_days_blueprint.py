from flask import Blueprint, jsonify, request
from werkzeug import Response
import json
from flask_api import status
from api.utils.response_formatter import response, response_text
from api.services.service_handler import ServiceHandler
from api.config.configuration import ROUTE_CONFIG
from api.utils.validate_fields import check_empty_string, check_empty_string_in_array, check_if_key_exists
from api.enums.user_enums import UserTypeEnum

route_name = ROUTE_CONFIG['USER_PREGNANCY_DAYS_TYPE_NAME']
app_usr_pregnancy_days = Blueprint(route_name,__name__, url_prefix='/api')

@app_usr_pregnancy_days.route('/{}/<user_id>'.format(route_name), methods=['GET'])
def get_last_user_pregnant_days(user_id):
    try:
        user = ServiceHandler.get_service(ROUTE_CONFIG['USER_TYPE_NAME']).get(user_id)

        if not user:
            raise Exception('User with id {} not found!'.format(user_id))

        obj = ServiceHandler.get_service(route_name).get_by_user(user)

        if not obj:
            raise Exception('User with id {} has no user_pregnancy_days records.'.format(user_id))

        if obj.user_id['user_type'] != UserTypeEnum.pregnant.value:
            raise Exception('This user is not pregnant to control user_pregnancy_days records')

        return response(obj.to_json(), status.HTTP_200_OK)
    except Exception as e:
        return response_text(str(e), status.HTTP_400_BAD_REQUEST)       

@app_usr_pregnancy_days.route(route_name, methods=['POST'])
def insert():
    try:        
        json_obj = request.get_json()

        check_if_key_exists('days', json_obj)
        check_if_key_exists('days_start', json_obj)
        check_if_key_exists('user_id', json_obj)

        user_id = json_obj['user_id']

        user = ServiceHandler.get_service(ROUTE_CONFIG['USER_TYPE_NAME']).get(user_id)

        if not user:
            raise Exception('User with id {} not found!'.format(user_id))

        days_obj = {
            'days':json_obj['days'],
            'days_start':json_obj['days_start'],
            'user' : user
        }

        ServiceHandler.get_service(route_name).insert(days_obj)

        return response(status=status.HTTP_200_OK)

    except Exception as e:
        return response_text(str(e), status.HTTP_400_BAD_REQUEST)



@app_usr_pregnancy_days.route('/{}/<id>'.format(route_name), methods=['PUT'])
def update(id):
    try:        
        json_obj = request.get_json()

        check_if_key_exists('days', json_obj)

        days_obj = {
            'days':json_obj['days'],
            'id' : id
        }

        ServiceHandler.get_service(route_name).update(days_obj)

        return response(status=status.HTTP_200_OK)

    except Exception as e:
        return response_text(str(e), status.HTTP_400_BAD_REQUEST)