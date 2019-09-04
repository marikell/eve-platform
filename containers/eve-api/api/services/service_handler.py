from api.services.generic_service import GenericService
from api.config.configuration import ROUTE_CONFIG
from api.services.answer_service import AnswerService
from api.services.entity_intent_answer_service import EntityIntentAnswerService
# from api.services.rasa_service import RasaService
from api.services.exam_service import ExamService
from api.services.user_service import UserService
from api.services.user_exam_service import UserExamService
from api.services.user_info_service import UserInfoService
from api.services.user_health_info_service import UserHealthInfoService
from api.services.user_pregnancy_info_service import UserPregnancyInfoService
from api.services.user_postpartum_info_service import UserPostpartumInfoService
from api.services.unanswered_question_service import UnansweredQuestionService
from api.services.user_trimester_service import UserTrimesterService
from api.services.form_service import FormService
from api.services.tip_service import TipService
from api.services.notification_user_service import NotificationUserService
from api.services.conversations_service import ConversationsService

services : dict = {}

class ServiceHandler():

    @staticmethod
    def register_services():
        services[ROUTE_CONFIG['ANSWER_TYPE_NAME']] = AnswerService()
        services[ROUTE_CONFIG['ENTITY_INTENT_ANSWER_TYPE_NAME']] = EntityIntentAnswerService()
        services[ROUTE_CONFIG['USER_TYPE_NAME']] = UserService()
        services[ROUTE_CONFIG['EXAM_TYPE_NAME']] = ExamService()
        services[ROUTE_CONFIG['USER_INFO_TYPE_NAME']] = UserInfoService()
        services[ROUTE_CONFIG['USER_HEALTH_INFO_TYPE_NAME']] = UserHealthInfoService()
        services[ROUTE_CONFIG['USER_PREGNANCY_INFO_TYPE_NAME']] = UserPregnancyInfoService()
        services[ROUTE_CONFIG['USER_POSTPARTUM_INFO_TYPE_NAME']] = UserPostpartumInfoService()
        services[ROUTE_CONFIG['USER_EXAM_TYPE_NAME']] = UserExamService()
        services[ROUTE_CONFIG['UNANSWERED_QUESTION_TYPE_NAME']] = UnansweredQuestionService()
        services[ROUTE_CONFIG['USER_TRIMESTER_TYPE_NAME']] = UserTrimesterService()
        services[ROUTE_CONFIG['TIP_TYPE_NAME']] = TipService()
        services[ROUTE_CONFIG['FORM_TYPE_NAME']] = FormService()
        services[ROUTE_CONFIG['NOTIFICATION_USER_TYPE_NAME']] = NotificationUserService()
        services[ROUTE_CONFIG['CONVERSATIONS_TYPE_NAME']] = ConversationsService()

    @staticmethod
    def get_service(name: str):
        return services[name]


    
