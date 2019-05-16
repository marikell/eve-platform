from mongoengine.queryset.visitor import Q
from models.entity_intent_answer import EntityIntentAnswer
from utils.mongo_encoder import jsonify
from services.generic_service import GenericService

class EntityIntentAnswerService(GenericService):
    def __init__(self):
        super().__init__()        

    def insert(self, obj):
        entity_insert_answer = EntityIntentAnswer(entities=obj['entities'], 
        intent=obj['intent'],answer_id=obj['answer'].to_dbref())
        entity_insert_answer.save() 
    def action_answer(self, entities, intent):
        return EntityIntentAnswer.objects.get(Q(entities__all=[entities]) & Q(intent=intent))