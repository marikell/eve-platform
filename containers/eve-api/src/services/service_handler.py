from services.generic_service import GenericService
from config.route_config import RouteConfig
from services.answer_service import AnswerService
from services.entity_intent_answer_service import EntityIntentAnswerService

services : dict = {}

class ServiceHandler():

    @staticmethod
    def register_services():
        services[RouteConfig.get('ANSWER_TYPE_NAME')] = AnswerService()
        services[RouteConfig.get('ENTITY_INTENT_ANSWER_TYPE_NAME')] = EntityIntentAnswerService()

    @staticmethod
    def get_service(name: str):
        return services[name]


    
