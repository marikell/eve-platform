from api.services.generic_service import GenericService
from api.config.configuration import ROUTE_CONFIG
from api.services.answer_service import AnswerService
from api.services.entity_intent_answer_service import EntityIntentAnswerService
from api.services.user_pregnancy_weeks_service import UserPregnancyWeeksService
from api.services.rasa_service import RasaService
from api.services.exam_service import ExamService
from api.services.user_service import UserService
from api.services.person_service import PersonService
from api.services.user_info_service import UserInfoService

services : dict = {}

class ServiceHandler():

    @staticmethod
    def register_services():
        services[ROUTE_CONFIG['ANSWER_TYPE_NAME']] = AnswerService()
        services[ROUTE_CONFIG['ENTITY_INTENT_ANSWER_TYPE_NAME']] = EntityIntentAnswerService()
        services[ROUTE_CONFIG['USER_TYPE_NAME']] = UserService()
        services[ROUTE_CONFIG['PERSON_TYPE_NAME']] = PersonService()
        services[ROUTE_CONFIG['USER_PREGNANCY_WEEKS_TYPE_NAME']] = UserPregnancyWeeksService()
        services[ROUTE_CONFIG['EXAM_TYPE_NAME']] = ExamService()
        services[ROUTE_CONFIG['RASA']] = RasaService()
        services[ROUTE_CONFIG['USER_INFO_TYPE_NAME']] = UserInfoService()

    @staticmethod
    def get_service(name: str):
        return services[name]


    
