from mongoengine.queryset.visitor import Q
from api.models.intent_answer import IntentAnswer
from api.services.generic_service import GenericService

class IntentAnswerService(GenericService):
    def __init__(self):
        super().__init__(IntentAnswer.objects)        

    def insert(self, obj):
        intent_answer = IntentAnswer(intent=obj['intent'],answer_id=obj['answer'].to_dbref())

        if IntentAnswer.objects(intent=obj['intent']):
            raise Exception('This intent are already in db.')
        
        intent_answer.save()

    def get_by_intent(self, intent):
        return IntentAnswer.objects(Q(intent=intent)).first()
    
    def update(self, obj):
        intent_answer = self.get(obj['id'])

        if not intent_answer:
            raise Exception('Object with id {} not found!'.format(obj['id']))

        intent_answer.intent = obj['intent']
        intent_answer.save()