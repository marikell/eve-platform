from flask import Blueprint, jsonify, request
from werkzeug import Response
from flask_api import status
from api.utils.response_formatter import response, response_text
from api.services.service_handler import ServiceHandler
from api.config.configuration import ROUTE_CONFIG
from api.utils.validate_fields import *

route_name = ROUTE_CONFIG['NOTIFICATION_USER_TYPE_NAME']
app_notification_user = Blueprint(route_name,__name__, url_prefix='/api')

@app_notification_user.route('/{}/<id>'.format(route_name), methods=['GET'])
def get_all_by_user(id):
    try:
        users = ServiceHandler.get_service(route_name).get_all_by_user(id).order_by('creation_date').only('_id','description','creation_date','title')

        return response(users, status.HTTP_200_OK)
                
    except Exception as e:
        return response_text(str(e), status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return response_text(str(e), status.HTTP_400_BAD_REQUEST)

@app_notification_user.route('/{}/<id>'.format(route_name), methods=['DELETE'])
def delete_by_user(id):
    try:
        ServiceHandler.get_service(route_name).delete_by_user(id)

        return response(status=status.HTTP_200_OK)

    except Exception as e:
        return response(str(e), status.HTTP_400_BAD_REQUEST)


@app_notification_user.route(route_name, methods=['POST'])
def insert():
    try:
        json = request.get_json()

        user = ServiceHandler.get_service(ROUTE_CONFIG['USER_TYPE_NAME']).get(json['user_id'])
        
        if not user:
            raise Exception('User not found!')

        obj = {
            "description": json['description'],
            "title" : json['title'],
            "user": user
        }

        ServiceHandler.get_service(route_name).insert(obj)    
        
        return response(status=status.HTTP_201_CREATED)

    except Exception as e:
        return response_text(str(e), status.HTTP_400_BAD_REQUEST)