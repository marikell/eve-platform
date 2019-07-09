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


@app_rasa.route('/{}/send-slot-user-exam/<id>'.format(route_name), methods=['POST'])
def send_user_exam_slot(id):
    try:
        json_obj = request.get_json()
        exam = ServiceHandler.get_service(ROUTE_CONFIG['EXAM_TYPE_NAME']).get(json_obj['exam_id'])

        if not exam:
            raise Exception('Exam not found!')

        user = ServiceHandler.get_service(ROUTE_CONFIG['USER_TYPE_NAME']).get(json_obj['user_id'])
        
        if not user:
            raise Exception('User not found!')

        obj = {
            'user' : user,
            'exam' : exam
        }

        ServiceHandler.get_service(ROUTE_CONFIG['USER_EXAM_TYPE_NAME']).insert(obj)      

        return response(status=status.HTTP_201_CREATED)

    except Exception as e:
        return response_text(str(e), status.HTTP_400_BAD_REQUEST)


@app_rasa.route('/{}/send-slots/<id>'.format(route_name), methods=['POST'])
def send_health_slots_from_Rasa(id):
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
            'last_menstruation_date' : None if 'last_menstruation_date' not in json_obj else json_obj['last_menstruation_date'],
            'first_ultrasound_date' : None if 'first_ultrasound_date' not in json_obj else json_obj['first_ultrasound_date'],
            'user' : user
        }

        user_info = ServiceHandler.get_service(ROUTE_CONFIG['USER_INFO_TYPE_NAME']).get_by_user(user)
            
        if user_info:
            obj['id'] = user_info.id
            ServiceHandler.get_service(ROUTE_CONFIG['USER_INFO_TYPE_NAME']).update(obj)
        else:
            ServiceHandler.get_service(ROUTE_CONFIG['USER_INFO_TYPE_NAME']).insert(obj)
        
        return response(status=status.HTTP_200_OK)

    except Exception as e:
        print(str(e))
        return response_text(str(e), status.HTTP_400_BAD_REQUEST)
    return None


@app_rasa.route('/{}/send-health-slots/<id>'.format(route_name), methods=['POST'])
def send_slots_from_Rasa(id):
    try:
        json_obj = request.get_json()
        user = ServiceHandler.get_service(ROUTE_CONFIG['USER_TYPE_NAME']).get(id)

        if not user:
            raise Exception('User not found!')

        obj = {
            'takes_regular_medicine' : False if 'takes_regular_medicine' not in json_obj else json_obj['takes_regular_medicine'],
            'regular_medicine_name' : None if 'regular_medicine_name' not in json_obj else json_obj['regular_medicine_name'],
            'has_hypothyroidism' : False if 'has_hypothyroidism' not in json_obj else json_obj['has_hypothyroidism'],
            'has_hyperthyroidism' : False if 'has_hyperthyroidism' not in json_obj else json_obj['has_hyperthyroidism'],
            'has_diabetes' : False if 'has_diabetes' not in json_obj else json_obj['has_diabetes'],
            'drug_use' : False if 'drug_use' not in json_obj else json_obj['drug_use'],
            'has_autoimmune_disease' : False if 'has_autoimmune_disease' not in json_obj else json_obj['has_autoimmune_disease'],
            'has_asthma' : False if 'has_asthma' not in json_obj else json_obj['has_asthma'],
            'is_seropositive' : False if 'is_seropositive' not in json_obj else json_obj['is_seropositive'],
            'has_high_pressure' : False if 'has_high_pressure' not in json_obj else json_obj['has_high_pressure'],
            'user' : user
        }

        user_health_info = ServiceHandler.get_service(ROUTE_CONFIG['USER_HEALTH_INFO_TYPE_NAME']).get_by_user(user)
            
        if user_health_info:
            obj['id'] = user_health_info.id
            ServiceHandler.get_service(ROUTE_CONFIG['USER_HEALTH_INFO_TYPE_NAME']).update(obj)
        else:
            ServiceHandler.get_service(ROUTE_CONFIG['USER_HEALTH_INFO_TYPE_NAME']).insert(obj)
        
        return response(status=status.HTTP_200_OK)

    except Exception as e:
        print(str(e))
        return response_text(str(e), status.HTTP_400_BAD_REQUEST)
    return None