from api.services.fup_service import get_users_exams
from api.config.configuration import ROUTE_CONFIG
from flask import Blueprint, jsonify, request
from werkzeug import Response
from flask_api import status
from bson import json_util
from api.services.exam_service import ExamService
import json
from api.utils.validate_fields import check_empty_string, check_if_key_exists
from api.utils.response_formatter import response, response_text


route_name = ROUTE_CONFIG['FUP']
app_fup = Blueprint(route_name,__name__, url_prefix='/api')

@app_fup.route('/{}/pregnant-users-with-exams'.format(route_name), methods=['GET'])
def get_pregnant_users():
    try:
        obj = get_users_exams()

        return response(json_util.dumps(obj),status=status.HTTP_200_OK)
        
    except Exception as e:
        return response(str(e), status.HTTP_400_BAD_REQUEST)


