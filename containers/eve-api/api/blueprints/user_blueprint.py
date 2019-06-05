from flask import Blueprint, jsonify, request
from werkzeug import Response
import json
from flask_api import status
from api.utils.response_formatter import response, response_text
from api.services.service_handler import ServiceHandler
from api.config.configuration import ROUTE_CONFIG
from api.enums.user_enums import UserTypeEnum
from api.utils.validate_fields import check_empty_string, check_empty_string_in_array, check_if_key_exists
from werkzeug.security import generate_password_hash, check_password_hash

route_name = ROUTE_CONFIG['USER_TYPE_NAME']
app_user = Blueprint(route_name,__name__, url_prefix='/api')

def validate_user_request(json):          
    keys = ['name', 'email','password','is_admin','confirm_password','user_type']
    for k in keys:
        if k is not 'is_admin' and k is not 'user_type':
            check_if_key_exists(k, json)
            check_empty_string(json[k], k)

    if json['confirm_password'] != json['password']:
        raise Exception("Passwords don't match. Try again")

@app_user.route('/{}'.format(route_name), methods=['GET'])
def get_all():
    try:
        users = ServiceHandler.get_service(route_name).get_all().only('_id','email','creation_date'
        ,'user_type','person_id','is_admin')

        return response(users, status.HTTP_200_OK)
                
    except Exception as e:
        return response_text(str(e), status.HTTP_400_BAD_REQUEST)

@app_user.route(route_name, methods=['POST'])
def insert():
    try:
        json = request.get_json()

        validate_user_request(json)

        person_obj = {
            'name': json['name']
        }

        created_person = ServiceHandler.get_service(ROUTE_CONFIG['PERSON_TYPE_NAME']).insert(person_obj)       

        hashed_password = generate_password_hash(json['password'], method='sha512')

        obj = {
            'email': json['email'],
            'password': hashed_password,
            'is_admin': (False if 'is_admin' not in json else json['is_admin']),
            'person': created_person,
            'user_type': (UserTypeEnum.normal.value if 'user_type' not in json else json['user_type'])
        }

        ServiceHandler.get_service(route_name).insert(obj)    
        
        return response(status=status.HTTP_201_CREATED)

    except Exception as e:
        return response_text(str(e), status.HTTP_400_BAD_REQUEST)

@app_user.route('/{}/<id>'.format(route_name), methods=['GET'])
def get(id):
    try:
        obj = ServiceHandler.get_service(route_name).get(id)

        if not obj:
            raise Exception('Object with id {} not found!'.format(id))

        return response(obj.to_json(), status.HTTP_200_OK)

    except Exception as e:
        return response(str(e), status.HTTP_400_BAD_REQUEST)

@app_user.route('/{}/<id>'.format(route_name), methods=['PUT'])
def update(id):
    try:
        json_obj = request.get_json()

        validate_user_request(json_obj)

        user = ServiceHandler.get_service(route_name).get(id)

        if not user:
            raise Exception('User not found!')
        
        person_id = str(user.person_id['id'])

        person_obj = {
            'name': json_obj['name'],
            'id': person_id
        }

        ServiceHandler.get_service(ROUTE_CONFIG['PERSON_TYPE_NAME']).update(person_obj)

        hashed_password = generate_password_hash(json_obj['password'], method='sha512')

        obj = {
            'email': json_obj['email'],
            'password': hashed_password,
            'is_admin': (False if 'is_admin' not in json_obj else json_obj['is_admin']),
            'id': id,
            'user_type': (UserTypeEnum.normal.value if 'user_type' not in json_obj else json_obj['user_type'])
        }

        ServiceHandler.get_service(route_name).update(obj)

        return response(status=status.HTTP_200_OK)

    except Exception as e:
        return response(str(e), status.HTTP_400_BAD_REQUEST)

@app_user.route('/{}/<id>'.format(route_name), methods=['DELETE'])
def delete(id):
    try:        
        user = ServiceHandler.get_service(route_name).get(id)

        person_id = str(user.person_id['id'])

        ServiceHandler.get_service(route_name).delete(id)
        ServiceHandler.get_service(ROUTE_CONFIG['PERSON_TYPE_NAME']).delete(person_id)

        return response(status=status.HTTP_200_OK)
        
    except Exception as e:
        return response(str(e), status.HTTP_400_BAD_REQUEST)
