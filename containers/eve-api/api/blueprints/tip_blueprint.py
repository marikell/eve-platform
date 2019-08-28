from flask import Blueprint, jsonify, request
from werkzeug import Response
from flask_api import status
from api.services.tip_service import TipService
from api.utils.response_formatter import response, response_text
from api.services.service_handler import ServiceHandler
from api.config.configuration import ROUTE_CONFIG
from api.utils.validate_fields import *

route_name = ROUTE_CONFIG['TIP_TYPE_NAME']
app_tip = Blueprint(route_name,__name__, url_prefix='/api')

@app_tip.route(route_name, methods=['POST'])
def insert():
    try:
        json = request.get_json()
        obj = {
            "description": json['description'],
            "tip_type": json['tip_type']
        }

        ServiceHandler.get_service(route_name).insert(obj)    
        
        return response(status=status.HTTP_201_CREATED)

    except Exception as e:
        return response_text(str(e), status.HTTP_400_BAD_REQUEST)

@app_tip.route('/{}/filtered-tip'.format(route_name), methods=['POST'])
def get_by_email():
    try:
        json_obj = request.get_json()

        obj = ServiceHandler.get_service(route_name).getby_type(json_obj['tip_type'])

        if not obj:
            raise Exception('Não há dicas para o tipo {}'.format(json_obj['tip_type']))

        return response(obj.to_json(), status.HTTP_200_OK)
      
    except Exception as e:
        return response(str(e), status.HTTP_400_BAD_REQUEST)

@app_tip.route('/{}/<id>'.format(route_name), methods=['PUT'])
def update(id):
    try:
        json = request.get_json()

        obj = {
             "id" : id,
            "send": json['send']
        }

        ServiceHandler.get_service(route_name).update(obj)

        return response(status=status.HTTP_200_OK)

    except Exception as e:
        return response(str(e), status.HTTP_400_BAD_REQUEST)

@app_tip.route('/{}/reset'.format(route_name), methods=['PUT'])
def reset():
    try:
        json = request.get_json()

        tip_type = json['tip_type']

        ServiceHandler.get_service(route_name).reset_by_type(tip_type)

        return response(status=status.HTTP_200_OK)

    except Exception as e:
        return response(str(e), status.HTTP_400_BAD_REQUEST)

@app_tip.route('/{}/<id>'.format(route_name), methods=['DELETE'])
def delete(id):
    try:        
        ServiceHandler.get_service(route_name).delete(id)

        return response(status=status.HTTP_200_OK)
        
    except Exception as e:
        return response(str(e), status.HTTP_400_BAD_REQUEST)
