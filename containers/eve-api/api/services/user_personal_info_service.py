from mongoengine.queryset.visitor import Q
from api.models.user_personal_info import UserPersonalInfo
from bson.objectid import ObjectId
from api.services.generic_service import GenericService

class UserPersonalInfoService(GenericService):
    def __init__(self):
        super().__init__(UserPersonalInfo.objects)
        
    def insert(self, obj):                                        
        
        height = (obj['height'])
        weight = (obj['weight'])
        date_birth = (obj['date_birth'])
        state = (obj['state'])
        
        user_personal_info = UserPersonalInfo(height=height, 
                             weight=weight,
                             date_birth=date_birth,
                             state=state,
                             user_id=obj['user'].to_dbref())
        
        user_personal_info.save()


    def get_by_user(self, user):
        return self.objects(Q(user_id=ObjectId(user.id))).first()

    def update(self, obj):
        user_personal_info = self.get(obj['id'])

        if not user_personal_info:
            raise Exception('Object with id {} not found!'.format(obj['id']))
        
        user_personal_info.height = (obj['height'])
        user_personal_info.weight = (obj['weight'])
        user_personal_info.date_birth = (obj['date_birth'])
        user_personal_info.state = (obj['state'])
        
        user_personal_info.save()