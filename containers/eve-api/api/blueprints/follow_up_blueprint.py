from api.config.configuration import ROUTE_CONFIG
from flask import Blueprint, jsonify, request
from werkzeug import Response
from flask_api import status
from api.services.service_handler import ServiceHandler
from api.utils.validate_fields import check_empty_string, check_if_key_exists
from api.utils.response_formatter import response, response_text


route_name = ROUTE_CONFIG['FOLLOW_UP_TYPE_NAME']
app_follow_up = Blueprint(route_name,__name__, url_prefix='/api')

def validate_followup_request(json):
    keys = ['weeks_start','name','followup_type']
    for k in keys:         
        check_if_key_exists(k, json)
        check_empty_string(k, json)

@app_follow_up.route('/{}'.format(route_name), methods=['GET'])
def index():
    return Response('Hello {}'.format(route_name))


@app_follow_up.route(route_name, methods=['POST'])
def insert():
    try:
        json_obj = request.get_json()

        validate_followup_request(json_obj)

        obj = {
            "weeks_start": json_obj['weeks_start'],
            "weeks_end": (None if 'weeks_end' not in json_obj else json_obj['weeks_end']),
            "description": ('' if 'description' not in json_obj else json_obj['description']),
            "name": json_obj['name'],
            "followup_type": json_obj['followup_type']
        }

        ServiceHandler.get_service(route_name).insert(obj)    
        
        return response(status=status.HTTP_201_CREATED)

    except Exception as e:
        return response_text(str(e), status.HTTP_400_BAD_REQUEST)

@app_follow_up.route('/{}/<id>'.format(route_name), methods=['DELETE'])
def delete(id):
    try:        
        ServiceHandler.get_service(route_name).delete(id)

        return response(status=status.HTTP_200_OK)
        
    except Exception as e:
        return response(str(e), status.HTTP_400_BAD_REQUEST)
