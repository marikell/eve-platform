#Classe destinada para manipulação de informações gerais do serviço, que misture diversas tabelas
from api.services.exam_service import ExamService
from api.services.user_service import UserService
from api.models.user_pregnancy_weeks import UserPregnancyWeeks
from api.services.user_pregnancy_weeks_service import UserPregnancyWeeksService
from bson import json_util

def get_users_exams():
    pipeline = [{
                '$unwind': '$user_id'
                },
                {'$lookup': 
                {'from' : 'user_exam',
                 'localField' : 'user_id',
                 'foreignField' : 'user_id',
                 'as' : 'user_exams'}}]

    join_result = [usr for usr in UserPregnancyWeeks._get_collection().aggregate(pipeline)]
    return join_result
        
    
