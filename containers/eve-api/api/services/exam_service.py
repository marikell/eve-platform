from api.models.exam import Exam
from api.services.generic_service import GenericService
from mongoengine.queryset.visitor import Q

class ExamService(GenericService):
    def __init__(self):
        super().__init__(Exam.objects)        

    def insert(self, obj):        
        exam = Exam(trimester=obj['trimester'], description=obj['description'], name=obj['name'])
        exam.save()

    def get_by_name(self, exam_name):
        return self.objects(Q(name=exam_name)).first()