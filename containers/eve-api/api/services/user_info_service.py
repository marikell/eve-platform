from mongoengine.queryset.visitor import Q
from api.models.user_info import UserInfo
from bson.objectid import ObjectId
from api.services.generic_service import GenericService

class UserInfoService(GenericService):
    def __init__(self):
        super().__init__(UserInfo.objects)
        
    def insert(self, obj):
        has_children = (obj['has_children'])
        has_health_plan = (obj['has_health_plan'])
        is_planning_with_doctor = (obj['is_planning'])
        is_pregnant = (obj['is_pregnant'])
        is_trying = (obj['is_trying'])
        is_postpartum = (obj['is_postpartum'])
        
        user_info = UserInfo(has_children=has_children,
                             has_health_plan=has_health_plan, 
                             is_planning_with_doctor=is_planning_with_doctor,
                             is_pregnant=is_pregnant,
                             is_trying=is_trying,
                             is_postpartum=is_postpartum,
                             user_id=obj['user'].to_dbref())
        user_info.save()

    def get_by_user_id(self, user_id):
        return self.objects(Q(user_id=ObjectId(user_id))).first()

    def update(self, obj):
        user_info = self.get(obj['id'])
        
        if not user_info:
            raise Exception('Object with id {} not found!'.format(obj['id']))
                
        user_info.height = (obj['height'])
        user_info.weight = (obj['weight'])
        user_info.state = (obj['state'])

        user_info.save()