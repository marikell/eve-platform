from flask import Blueprint, jsonify, request
from werkzeug import Response
from flask_api import status
from api.services.answer_service import AnswerService
from api.services.user_service import UserService
from api.utils.response_formatter import response, response_text
from api.utils.response_formatter import response, response_text
from api.services.service_handler import ServiceHandler
from api.config.configuration import ROUTE_CONFIG
from api.utils.validate_fields import *

route_name = ROUTE_CONFIG['RASA']
app_rasa = Blueprint(route_name,__name__, url_prefix='/api')

@app_rasa.route('/{}/send-slots/<id>'.format(route_name), methods=['POST'])
def send_slots_from_Rasa(id):
    try:
        json_obj = request.get_json()
        user = ServiceHandler.get_service(ROUTE_CONFIG['USER_TYPE_NAME']).get(id)

        if not user:
            raise Exception('User not found!')

        obj = {

            'is_first_pregnancy' : False if 'is_first_pregnancy' not in json_obj else json_obj['is_first_pregnancy'],
            'has_children' : False if 'has_children' not in json_obj else json_obj['has_children'],
            'has_health_plan' : False if 'has_health_plan' not in json_obj else json_obj['has_health_plan'],
            'is_planning' : False if 'is_planning' not in json_obj else json_obj['is_planning'],
            'is_pregnant' : False if 'is_pregnant' not in json_obj else json_obj['is_pregnant'],
            'is_trying' : False if 'is_trying' not in json_obj else json_obj['is_trying'],
            'is_planned_pregnancy' : False if 'is_planned_pregnancy' not in json_obj else json_obj['is_planned_pregnancy'],
            'is_doing_pre_natal' : False if 'is_doing_pre_natal' not in json_obj else json_obj['is_doing_pre_natal'],
            'user' : user
        }

        days_obj = {
            'weeks': False if 'pregnancy_weeks' not in json_obj else json_obj['pregnancy_weeks'],
            'weeks_start': False if 'pregnancy_weeks' not in json_obj else json_obj['pregnancy_weeks'],
            'user' : user
        }

        user_info = ServiceHandler.get_service(ROUTE_CONFIG['USER_INFO_TYPE_NAME']).get_by_user(user)
            
        if user_info:
            obj['id'] = user_info.id
            ServiceHandler.get_service(ROUTE_CONFIG['USER_INFO_TYPE_NAME']).update(obj)        
        else:
            ServiceHandler.get_service(ROUTE_CONFIG['USER_INFO_TYPE_NAME']).insert(obj)      

        user_weeks = ServiceHandler.get_service(ROUTE_CONFIG['USER_PREGNANCY_WEEKS_TYPE_NAME']).get_by_user(user)

        if user_weeks:
            days_obj['id'] = user_weeks.id
            if bool(json_obj['is_pregnant']):
                ServiceHandler.get_service(ROUTE_CONFIG['USER_PREGNANCY_WEEKS_TYPE_NAME']).update_slots(days_obj)
            else:
                ServiceHandler.get_service(ROUTE_CONFIG['USER_PREGNANCY_WEEKS_TYPE_NAME']).delete(user_weeks.id)
        else:
            ServiceHandler.get_service(ROUTE_CONFIG['USER_PREGNANCY_WEEKS_TYPE_NAME']).insert(days_obj)   

        return response(status=status.HTTP_200_OK)

    except Exception as e:
        print(str(e))
        return response_text(str(e), status.HTTP_400_BAD_REQUEST)
    return None