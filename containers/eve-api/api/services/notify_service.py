from api.models.user import User
from bson import json_util


def get_users_infos():
    pipeline = [
        {
            '$lookup': {
                'from': 'user_info',
                'localField': '_id',
                'foreignField': 'user_id',
                'as': 'user_infos'
            }
        },
        {
            '$unwind': '$_id'
        },
        {
            '$project': {
                'user_id': 1,
                '_id': 1,
                'user_infos.is_pregnant': 1,
                'user_infos.is_trying': 1,
                'email' : 1
            }
        }
    ]

    join_result = [
        usr for usr in User._get_collection().aggregate(pipeline)]
    return join_result
