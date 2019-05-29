from api.services.generic_service import GenericService
from api.config.configuration import ROUTE_CONFIG
from api.services.answer_service import AnswerService
from api.services.entity_intent_answer_service import EntityIntentAnswerService

services : dict = {}

class ServiceHandler():

    @staticmethod
    def register_services():
        services[ROUTE_CONFIG['ANSWER_TYPE_NAME']] = AnswerService()
        services[ROUTE_CONFIG['ENTITY_INTENT_ANSWER_TYPE_NAME']] = EntityIntentAnswerService()

    @staticmethod
    def get_service(name: str):
        return services[name]


    
