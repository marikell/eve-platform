from services.generic_service import GenericService
from config.configuration import ROUTE_CONFIG
from services.answer_service import AnswerService
from services.entity_intent_answer_service import EntityIntentAnswerService

services : dict = {}

class ServiceHandler():

    @staticmethod
    def register_services():
        services[ROUTE_CONFIG['ANSWER_TYPE_NAME']] = AnswerService()
        services[ROUTE_CONFIG['ENTITY_INTENT_ANSWER_TYPE_NAME']] = EntityIntentAnswerService()

    @staticmethod
    def get_service(name: str):
        return services[name]


    
