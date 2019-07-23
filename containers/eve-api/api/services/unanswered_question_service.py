from mongoengine.queryset.visitor import Q
from api.models.unanswered_question import UnansweredQuestion
from api.services.generic_service import GenericService

class UnansweredQuestionService(GenericService):
    def __init__(self):
        super().__init__(UnansweredQuestion.objects)        

    def insert(self, obj):        
        unanswered_question = UnansweredQuestion(question=obj['question'])
        unanswered_question.save()

    def update(self, obj):
        unanswered_question = self.get(obj['id'])

        if not unanswered_question:
            raise Exception('Object with id {} not found!'.format(obj['id']))
        
        unanswered_question.question = obj['question']
        unanswered_question.save()