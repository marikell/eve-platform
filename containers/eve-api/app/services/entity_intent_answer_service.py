from mongoengine.queryset.visitor import Q
from models.entity_intent_answer import EntityIntentAnswer
from services.generic_service import GenericService

class EntityIntentAnswerService(GenericService):
    def __init__(self):
        super().__init__(EntityIntentAnswer.objects)        

    def insert(self, obj):
        entity_intent_answer = EntityIntentAnswer(entities=obj['entities'], 
        intent=obj['intent'],answer_id=obj['answer'].to_dbref())

        if EntityIntentAnswer.objects(entities=obj['entities'], intent=obj['intent']):
            raise Exception('This entities and intent are already in db.')
        
        entity_intent_answer.save()

    def getby_intent_entities(self, entities, intent):
        return EntityIntentAnswer.objects(Q(entities__all=[entities]) & Q(intent=intent)).first()

    
    def update(self, obj):
        entity_intent_answer = self.get(obj['id'])

        if not entity_intent_answer:
            raise Exception('Object with id {} not found!'.format(obj['id']))

        entity_intent_answer.entities = obj['entities']
        entity_intent_answer.intent = obj['intent']

        entity_intent_answer.save()