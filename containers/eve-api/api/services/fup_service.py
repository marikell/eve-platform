#Classe destinada para manipulação de informações gerais do serviço, que misture diversas tabelas
from api.services.exam_service import ExamService
from api.services.user_service import UserService
from api.models.user_info import UserInfo
from api.models.user_exam import UserExam
from api.models.user_trimester import UserTrimester
from api.models.user import User
from bson import json_util

#consulta os usuários que tem registro na tabela user_trimester e qual o próximo exame a ser feito
def get_users_exams():
    pipeline = [
        {
            '$lookup': {
                'from' : 'exam',
                'let': { 'user_value': "$trimester" },
                'pipeline': [
                    {
                        '$match': {
                            '$expr': {
                                '$lte': [ "$trimester", "$$user_value" ]
                            }
                        }
                    },
                    { '$project': { 'trimester': 0, 'description': 0 } },
                    { '$limit': 1 },
                ],
                'as' : 'exm',
            }
        },
        {
            '$project' : {
                '_id': 0,
                'update_date': 0,
                'start_date': 0
            }
        },
    ]
    join_result = [usr for usr in UserTrimester._get_collection().aggregate(pipeline)]
    return join_result

# def get_users_infos():
#     pipeline = [
#         {
#             '$lookup': {
#                 'from' : 'user_info',
#                 'localField': 'user_id',
#                 'foreignField' : '_id',
#                 'as' : 'user_infos'
#             }
#         },
#         {
#             '$unwind':'$user_id'
#         }
#     ]
    
#     join_result = [usr for usr in User._get_collection().aggregate(pipeline)]
#     return join_result
