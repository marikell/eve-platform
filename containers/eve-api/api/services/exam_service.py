from api.models.exam import Exam
from api.services.generic_service import GenericService
from mongoengine.queryset.visitor import Q
from api.models.user_exam import UserExam
from bson.objectid import ObjectId

class ExamService(GenericService):
    def __init__(self):
        super().__init__(Exam.objects)        

    def insert(self, obj):        
        exam = Exam(trimester=obj['trimester'], description=obj['description'], name=obj['name'])
        exam.save()

    def get_by_name(self, exam_name):
        return self.objects(Q(name=exam_name)).first()


    def get_user_done_exams(self, user_id):
        pipeline = [
                {              
                '$lookup': {
                    'from': 'user_exam',
                    'localField': '_id',
                    'foreignField': 'exam_id',
                    'as': 'user_exams'},
                },              
                 {
                    '$unwind':'$user_exams'
                },
                {
                    '$match' : {'user_exams.user_id' : ObjectId(user_id)}
                }
                ]
        join_result = [exm for exm in Exam._get_collection().aggregate(pipeline)]
        print(join_result)
        return join_result