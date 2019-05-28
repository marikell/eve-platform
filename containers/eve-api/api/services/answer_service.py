from mongoengine.queryset.visitor import Q
from api.models.entity_intent_answer import EntityIntentAnswer
from api.services.generic_service import GenericService
from api.models.answer import Answer
from bson.objectid import ObjectId  

class AnswerService(GenericService):
    def __init__(self):
        super().__init__(Answer.objects)       

    def insert(self, obj):
        answer = Answer(text=obj['text'])
        answer.save()

    def update(self, obj):
        answer = self.get(obj['id'])

        if not answer:
            raise Exception('Object with id {} not found!'.format(obj['id']))

        answer.text = obj['text']
        answer.save()