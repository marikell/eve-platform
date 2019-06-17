from mongoengine.queryset.visitor import Q
from api.models.user_exam import UserExam
from bson.objectid import ObjectId
from api.services.generic_service import GenericService

class UserExamService(GenericService):
    def __init__(self):
        super().__init__(UserExam.objects)
        
    def insert(self, obj):
        user_exam = UserExam(user_id=obj['user'].to_dbref(), exam_id=obj['exam'].to_dbref())

        user_exam.save()