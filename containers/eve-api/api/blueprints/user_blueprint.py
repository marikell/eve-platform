from flask import Blueprint, jsonify, request, make_response
from werkzeug import Response
import json
from flask_api import status
from api.config.configuration import API_SECRET_KEY
from api.utils.response_formatter import response, response_text
from api.services.service_handler import ServiceHandler
from api.config.configuration import ROUTE_CONFIG
from api.enums.user_enums import UserTypeEnum
from api.utils.validate_fields import check_empty_string, check_empty_string_in_array, check_if_key_exists
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from functools import wraps
import datetime

route_name = ROUTE_CONFIG['USER_TYPE_NAME']
app_user = Blueprint(route_name,__name__, url_prefix='/api')


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        
        if not token:
            return response_text('Token is missing', status.HTTP_401_UNAUTHORIZED)
        
        try:
            data = jwt.decode(token, API_SECRET_KEY)
            current_user = ServiceHandler.get_service(route_name).get(data['id'])

        except:
            return response_text('Token is invalid!', status.HTTP_401_UNAUTHORIZED)

        return f(current_user, *args, **kwargs)

    return decorated


def validate_user_request(json):          
    keys = ['name', 'email','password', 'confirm_password','user_type']
    for k in keys:
        if k is not 'user_type':
            check_if_key_exists(k, json)
            check_empty_string(json[k], k)

    if json['confirm_password'] != json['password']:
        raise Exception("Passwords don't match. Try again")

@app_user.route('/verify-token')
def verify_token():
    obj = {
        "is_valid" : True
    }
    try:
        json = request.get_json()
        token = json['token']
        data = jwt.decode(token, API_SECRET_KEY)

        obj['is_valid'] = True
       
    except:
        obj['is_valid'] = False
        
    finally:
        return response(obj, status.HTTP_200_OK)

@app_user.route('/login')
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return response_text('UNAUTHORIZED', status.HTTP_401_UNAUTHORIZED)

    user = ServiceHandler.get_service(route_name).getby_email(auth.username)

    if not user:
        return response_text('E-mail inválido. Tente novamente!', status.HTTP_401_UNAUTHORIZED)
        # return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'}) 
    
    if check_password_hash(user['password'], auth.password):
        user_json = json.loads(user.to_json())
        user_id = user_json['_id']['$oid']
        token = jwt.encode({'id': user_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=1)}, API_SECRET_KEY)

        return jsonify({'token': token.decode('UTF-8'), 'name': user_json['name'], 'email' : user_json['email'] })        
    
    return response_text('Senha incorreta. Tente novamente!', status.HTTP_401_UNAUTHORIZED)


@app_user.route('/{}'.format(route_name), methods=['GET'])
@token_required
def get_all(current_user):
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
        # created_person = ServiceHandler.get_service(ROUTE_CONFIG['PERSON_TYPE_NAME']).insert(person_obj)       

        hashed_password = generate_password_hash(json['password'], method='sha512')

        obj = {
            'email': json['email'],
            'name' : json['name'],
            'birthDate' : datetime.datetime.strptime(json['birthDate'], '%d-%m-%Y'),
            'password': hashed_password,
            'user_type': (UserTypeEnum.normal.value if 'user_type' not in json else json['user_type'])
        }

        ServiceHandler.get_service(route_name).insert(obj)    
        
        return response(status=status.HTTP_201_CREATED)

    except Exception as e:
        return response_text(str(e), status.HTTP_400_BAD_REQUEST)

@app_user.route('/{}/get-by-email'.format(route_name), methods=['POST'])
def get_by_email():
    try:
        json_obj = request.get_json()

        check_if_key_exists('email', json_obj)

        obj = ServiceHandler.get_service(route_name).getby_email(json_obj['email'])

        if not obj:
            raise Exception('Object with email {} not found!'.format(json_obj['email']))

        return response(obj.to_json(), status.HTTP_200_OK)
      
    except Exception as e:
        return response(str(e), status.HTTP_400_BAD_REQUEST)

@app_user.route('/{}/<id>'.format(route_name), methods=['GET'])
def get(id):
    try:
        obj = ServiceHandler.get_service(route_name).get(id)

        if not obj:
            raise Exception('Object with ieyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjVkM2Y3ZmExMmQ4NDIzMzQxZTU2MzY5ZiIsImV4cCI6MTU2NTUzNTg2NX0.VkfUJLOLghmD1NSmQmdAnolCgnDgypWdqd-IREH7iygd {} not found!'.format(id))

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
