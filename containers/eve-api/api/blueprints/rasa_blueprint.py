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
from datetime import datetime
from dateutil.parser import parse
from datetime import date
from dateutil.relativedelta import relativedelta

route_name = ROUTE_CONFIG['RASA']
app_rasa = Blueprint(route_name,__name__, url_prefix='/api')

@app_rasa.route('/{}/send-slot-user-exam'.format(route_name), methods=['POST'])
def send_user_exam_slot():
    try:
        json_obj = request.get_json()
        user_exam = ServiceHandler.get_service(ROUTE_CONFIG['USER_EXAM_TYPE_NAME']).get(json_obj['id'])

        if not user_exam:
            raise Exception('User Exam not found!')

        obj = {
            'exam_status' : json_obj['exam_status'],
            'id' : json_obj['id']
        }

        ServiceHandler.get_service(ROUTE_CONFIG['USER_EXAM_TYPE_NAME']).update(obj)
        return response(status=status.HTTP_201_CREATED)

    except Exception as e:
        return response_text(str(e), status.HTTP_400_BAD_REQUEST)


@app_rasa.route('/{}/send-slots/<id>'.format(route_name), methods=['POST'])
def send_slots_from_Rasa(id):
    try:
        json_obj = request.get_json()
        user = ServiceHandler.get_service(ROUTE_CONFIG['USER_TYPE_NAME']).get(id)

        if not user:
            raise Exception('User not found!')
        
        obj_user_info = {
            'has_children' : False if 'has_children' not in json_obj else json_obj['has_children'],
            'has_health_plan' : False if 'has_health_plan' not in json_obj else json_obj['has_health_plan'],
            'is_planning' : False if 'is_planning' not in json_obj else json_obj['is_planning'],
            'is_pregnant' : False if 'is_pregnant' not in json_obj else json_obj['is_pregnant'],
            'is_trying' : False if 'is_trying' not in json_obj else json_obj['is_trying'],
            'is_postpartum' : False if 'is_postpartum' not in json_obj else json_obj['is_postpartum'],
            'user' : user
        }
        
        user_info = ServiceHandler.get_service(ROUTE_CONFIG['USER_INFO_TYPE_NAME']).get_by_user_id(user.id)
        if user_info:
            obj_user_info['id'] = user_info.id
            ServiceHandler.get_service(ROUTE_CONFIG['USER_INFO_TYPE_NAME']).update(obj_user_info)
        else:
            ServiceHandler.get_service(ROUTE_CONFIG['USER_INFO_TYPE_NAME']).insert(obj_user_info)
        
        if json_obj['is_pregnant']:
            obj_pregnancy_info = {
                'is_first_pregnancy' : False if 'is_first_pregnancy' not in json_obj else json_obj['is_first_pregnancy'],
                'is_planned_pregnancy' : False if 'is_planned_pregnancy' not in json_obj else json_obj['is_planned_pregnancy'],
                'is_doing_pre_natal' : False if 'is_doing_pre_natal' not in json_obj else json_obj['is_doing_pre_natal'],
                'last_menstruation_date' : None if 'last_menstruation_date' not in json_obj else json_obj['last_menstruation_date'],
                'first_ultrasound_date' : None if 'first_ultrasound_date' not in json_obj else json_obj['first_ultrasound_date'],
                'user' : user
            }
            
            user_pregnancy_info = ServiceHandler.get_service(ROUTE_CONFIG['USER_PREGNANCY_INFO_TYPE_NAME']).get_by_user_id(user.id)
            if user_pregnancy_info:
                obj_pregnancy_info['id'] = user_pregnancy_info.id
                ServiceHandler.get_service(ROUTE_CONFIG['USER_PREGNANCY_INFO_TYPE_NAME']).update(obj_pregnancy_info)
            else:
                ServiceHandler.get_service(ROUTE_CONFIG['USER_PREGNANCY_INFO_TYPE_NAME']).insert(obj_pregnancy_info)

            user_trimester = ServiceHandler.get_service(ROUTE_CONFIG['USER_TRIMESTER_TYPE_NAME']).get_by_user_id(user.id)
            if not user_trimester:
                last_menstruation_date = parse(obj_pregnancy_info['last_menstruation_date']).date()
                if last_menstruation_date > date.today():
                    last_menstruation_date = last_menstruation_date - relativedelta(years=1)
                
                if not obj_pregnancy_info['first_ultrasound_date']:
                    start_date = last_menstruation_date
                else:
                    first_ultrasound_date = parse(obj_pregnancy_info['first_ultrasound_date']).date()
                    if first_ultrasound_date > date.today():
                        first_ultrasound_date = first_ultrasound_date - relativedelta(years=1)
                    
                    date_diff = first_ultrasound_date - last_menstruation_date
                    start_date = first_ultrasound_date if date_diff.days > 7 else last_menstruation_date
                
                if ((date.today() - start_date).days <= 90):
                    trimester = 1
                elif ((date.today() - start_date).days <= 180):
                    trimester = 2
                else:
                    trimester = 3
                
                obj = {
                    'start_date' : start_date.strftime("%Y-%m-%dT%H:%M:%S.%f"),
                    'trimester' : trimester,
                    'user': user
                }
            
                ServiceHandler.get_service(ROUTE_CONFIG['USER_TRIMESTER_TYPE_NAME']).insert(obj)
            
        if json_obj['is_postpartum']:
            obj_postpartum_info = {
                'is_breastfeeding' : False if 'is_breastfeeding' not in json_obj else json_obj['is_breastfeeding'],
                'is_having_sex' : False if 'is_having_sex' not in json_obj else json_obj['is_having_sex'],
                'contraceptive_method' : None if 'contraceptive_method' not in json_obj else json_obj['contraceptive_method'],            
                'had_doctor_appointment' : False if 'had_doctor_appointment' not in json_obj else json_obj['had_doctor_appointment'],
                'had_infection' : False if 'had_infection' not in json_obj else json_obj['had_infection'],
                'infection_kind' : None if 'infection_kind' not in json_obj else json_obj['infection_kind'],
                'user' : user
            }

            user_postpartum_info = ServiceHandler.get_service(ROUTE_CONFIG['USER_POSTPARTUM_INFO_TYPE_NAME']).get_by_user_id(user.id)
            if user_postpartum_info:
                obj_postpartum_info['id'] = user_postpartum_info.id
                ServiceHandler.get_service(ROUTE_CONFIG['USER_POSTPARTUM_INFO_TYPE_NAME']).update(obj_postpartum_info)
            else:
                ServiceHandler.get_service(ROUTE_CONFIG['USER_POSTPARTUM_INFO_TYPE_NAME']).insert(obj_postpartum_info)
        
        return response(status=status.HTTP_200_OK)

    except Exception as e:
        print(str(e))
        return response_text(str(e), status.HTTP_400_BAD_REQUEST)
    return None


@app_rasa.route('/{}/send-health-slots/<id>'.format(route_name), methods=['POST'])
def send_health_slots_from_Rasa(id):
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

        user_health_info = ServiceHandler.get_service(ROUTE_CONFIG['USER_HEALTH_INFO_TYPE_NAME']).get_by_user_id(user.id)
            
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

@app_rasa.route('/{}/send-pregnancy-slots/<id>'.format(route_name), methods=['POST'])
def send_pregnancy_slots_from_Rasa(id):
    try:
        json_obj = request.get_json()
        
        user = ServiceHandler.get_service(ROUTE_CONFIG['USER_TYPE_NAME']).get(id)

        if not user:
            raise Exception('User not found!')

        obj = {
            'current_high_risk' : False if 'current_high_risk' not in json_obj else json_obj['current_high_risk'],
            'due_date' : None if 'due_date' not in json_obj else json_obj['due_date'],
            'births' : None if 'births' not in json_obj else json_obj['births'],
            'cesarean_births' : None if 'cesarean_births' not in json_obj else json_obj['cesarean_births'],
            'normal_births' : None if 'normal_births' not in json_obj else json_obj['normal_births'],
            'why_cesarean_birth' : None if 'why_cesarean_birth' not in json_obj else json_obj['why_cesarean_birth'],
            'abortion' : False if 'abortion' not in json_obj else json_obj['abortion'],
            'premature_birth' : False if 'premature_birth' not in json_obj else json_obj['premature_birth'],
            'user' : user
        }
        print(obj)
        user_pregnancy_info = ServiceHandler.get_service(ROUTE_CONFIG['USER_PREGNANCY_INFO_TYPE_NAME']).get_by_user_id(user.id)
            
        if user_pregnancy_info:
            obj['id'] = user_pregnancy_info.id
            ServiceHandler.get_service(ROUTE_CONFIG['USER_PREGNANCY_INFO_TYPE_NAME']).update(obj)
        else:
            ServiceHandler.get_service(ROUTE_CONFIG['USER_PREGNANCY_INFO_TYPE_NAME']).insert(obj)
        
        return response(status=status.HTTP_200_OK)

    except Exception as e:
        print(str(e))
        return response_text(str(e), status.HTTP_400_BAD_REQUEST)
    return None

@app_rasa.route('/{}/send-personal-slots/<id>'.format(route_name), methods=['POST'])
def send_personal_slots_from_Rasa(id):
    try:
        json_obj = request.get_json()
        user = ServiceHandler.get_service(ROUTE_CONFIG['USER_TYPE_NAME']).get(id)

        if not user:
            raise Exception('User not found!')

        obj = {
            'height' : None if 'height' not in json_obj else json_obj['height'],
            'weight' : None if 'weight' not in json_obj else json_obj['weight'],
            'state' : None if 'state' not in json_obj else json_obj['state'],
            'user' : user
        }
        
        user_info = ServiceHandler.get_service(ROUTE_CONFIG['USER_INFO_TYPE_NAME']).get_by_user_id(user.id)
            
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