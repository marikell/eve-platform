from mongoengine.queryset.visitor import Q
from api.models.user_info import UserInfo
from bson.objectid import ObjectId
from api.services.generic_service import GenericService

class UserInfoService(GenericService):
    def __init__(self):
        super().__init__(UserInfo.objects)
        
    def insert(self, obj):
        
        is_first_pregnancy = (obj['is_first_pregnancy'])
        has_children = (obj['has_children'])
        has_health_plan = (obj['has_health_plan'])
        is_planning_with_doctor = (obj['is_planning'])
        is_pregnant = (obj['is_pregnant'])
        is_trying = (obj['is_trying'])
        is_planned_pregnancy = (obj['is_planned_pregnancy'])
        is_doing_pre_natal = (obj['is_doing_pre_natal'])
        last_menstruation_date = (obj['last_menstruation_date'])
        first_ultrasound_date = (obj['first_ultrasound_date'])
        
        user_info = UserInfo(is_first_pregnancy=is_first_pregnancy, 
                             has_children=has_children,
                             has_health_plan=has_health_plan, 
                             is_planning_with_doctor=is_planning_with_doctor,
                             is_pregnant=is_pregnant,
                             is_trying=is_trying,
                             is_planned_pregnancy=is_planned_pregnancy,
                             is_doing_pre_natal=is_doing_pre_natal,
                             last_menstruation_date=last_menstruation_date,
                             first_ultrasound_date=first_ultrasound_date,
                             user_id=obj['user'].to_dbref())        
        
        user_info.save()


    def get_by_user(self, user):
        return self.objects(Q(user_id=ObjectId(user.id))).first()

    def update(self, obj):
        user_info = self.get(obj['id'])

        if not user_info:
            raise Exception('Object with id {} not found!'.format(obj['id']))
        
        user_info.is_first_pregnancy = (obj['is_first_pregnancy'])
        user_info.has_children = (obj['has_children'])
        user_info.is_planning_with_doctor = (obj['is_planning'])
        user_info.has_health_plan = (obj['has_health_plan'])
        user_info.is_pregnant = (obj['is_pregnant'])
        user_info.is_trying = (obj['is_trying'])
        user_info.is_planned_pregnancy = (obj['is_planned_pregnancy'])
        user_info.is_doing_pre_natal = (obj['is_doing_pre_natal'])
        user_info.last_menstruation_date = (obj['last_menstruation_date'])
        user_info.first_ultrasound_date = (obj['first_ultrasound_date'])

        user_info.save()