#Classe destinada para manipulação de informações gerais do serviço, que misture diversas tabelas
from api.services.exam_service import ExamService
from api.services.user_service import UserService
from api.models.user_pregnancy_weeks import UserPregnancyWeeks
from api.services.user_pregnancy_weeks_service import UserPregnancyWeeksService
from bson import json_util

def get_users_exams():
    pipeline = [
        {
            '$lookup': {
                'from' : 'user_exam',
                'localField': 'user_id',
                'foreignField' : 'user_id',
                'as' : 'user_exams'
            }
        },
        {
            '$unwind':'$user_id'
        },
        {
            '$lookup': {
                'from' : 'conversations',
                'localField': 'user_id',
                'foreignField' : 'sender_id',
                'as' : 'user_conversations'
            }
        },
        {
            '$project' : {
                'user_id' : 1,
                '_id' : 1,
                'weeks' : 1,
                'user_conversations._id' : 1,
                'user_exams.exam_id' : 1,
                'user_exams.is_done' : 1
            }
        }
    ]
    
    join_result = [usr for usr in UserPregnancyWeeks._get_collection().aggregate(pipeline)]
    return join_result

# def get_users_conversations
        
    
