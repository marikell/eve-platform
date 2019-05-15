from mongoengine.queryset.visitor import Q
from models.entity_intent_answer import EntityIntentAnswer
from utils.mongo_encoder import jsonify
from services.generic_service import GenericService
from models.answer import Answer
from bson.objectid import ObjectId  

class AnswerService(GenericService):
    def __init__(self):
        super().__init__()       

    def insert(self, obj):
        answer = Answer(text=obj['text'])
        answer.save()
    def get(self, id):
        answer = Answer.objects(Q(_id=ObjectId(id))).first()
        return answer