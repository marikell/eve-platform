from mongoengine.queryset.visitor import Q
from models.entity_intent_answer import EntityIntentAnswer
from utils.mongo_encoder import jsonify
from services.generic_service import GenericService
from models.answer import Answer
from bson.objectid import ObjectId  

class AnswerService(GenericService):
    def __init__(self):
        super().__init__(Answer.objects)       

    def insert(self, obj):
        answer = Answer(text=obj['text'])
        answer.save()