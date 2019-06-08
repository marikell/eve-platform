from api.models.exam import Exam
from api.services.generic_service import GenericService

class ExamService(GenericService):
    def __init__(self):
        super().__init__(Exam.objects)        

    def insert(self, obj):        
        exam = Exam(weeks_start=obj['weeks_start'], weeks_end=obj['weeks_end'],description=obj['description'], 
        name=obj['name'])        
        
        exam.save()