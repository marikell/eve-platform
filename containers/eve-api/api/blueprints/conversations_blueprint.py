from flask import Blueprint, jsonify, request
from werkzeug import Response
from flask_api import status
from api.utils.response_formatter import response, response_text
from api.services.service_handler import ServiceHandler
from api.config.configuration import ROUTE_CONFIG
from api.utils.validate_fields import *

route_name = ROUTE_CONFIG['CONVERSATIONS_TYPE_NAME']
app_conversations = Blueprint(route_name,__name__, url_prefix='/api')

@app_conversations.route('/{}/<id>'.format(route_name), methods=['DELETE'])
def delete_by_user(id):
    try:
        ServiceHandler.get_service(route_name).delete_by_senderid(id)

        return response(status=status.HTTP_200_OK)

    except Exception as e:
        return response(str(e), status.HTTP_400_BAD_REQUEST)