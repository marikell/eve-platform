from api.config.configuration import ROUTE_CONFIG
from flask import Blueprint, jsonify, request
from werkzeug import Response
from flask_api import status
from api.services.service_handler import ServiceHandler
from api.utils.validate_fields import check_empty_string, check_if_key_exists
from api.utils.response_formatter import response, response_text

route_name = ROUTE_CONFIG['FORM_TYPE_NAME']
app_form = Blueprint(route_name,__name__, url_prefix='/api')

def validate_followup_request(json):
    keys = ['trimester','name']
    for k in keys:         
        check_if_key_exists(k, json)
        check_empty_string(k, json)

@app_form.route('/{}/get-by-name'.format(route_name), methods=['POST'])
def get_by_name():
    try:
        form_name = str(request.get_json()['form_name'])
        form = ServiceHandler.get_service(route_name).get_by_name(form_name)

        return response(exam, status.HTTP_200_OK)
    except Exception as e:
        return response_text(str(e), status.HTTP_400_BAD_REQUEST)

@app_form.route('/{}'.format(route_name), methods=['GET'])
def get_all():
    try:
        forms = ServiceHandler.get_service(route_name).get_all()
        return response(exams, status.HTTP_200_OK)
    except Exception as e:
        return response_text(str(e), status.HTTP_400_BAD_REQUEST)

@app_form.route(route_name, methods=['POST'])
def insert():
    try:
        json_obj = request.get_json()
        validate_followup_request(json_obj)
        obj = {
            "trimester": json_obj['trimester'],
            "name": json_obj['name']
        }
        ServiceHandler.get_service(route_name).insert(obj)
        return response(status=status.HTTP_201_CREATED)
    except Exception as e:
        return response_text(str(e), status.HTTP_400_BAD_REQUEST)

@app_form.route('/{}/<id>'.format(route_name), methods=['DELETE'])
def delete(id):
    try:
        ServiceHandler.get_service(route_name).delete(id)

        return response(status=status.HTTP_200_OK)
        
    except Exception as e:
        return response(str(e), status.HTTP_400_BAD_REQUEST)
