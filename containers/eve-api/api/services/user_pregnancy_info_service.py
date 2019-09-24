from mongoengine.queryset.visitor import Q
from api.models.user_pregnancy_info import UserPregnancyInfo
from bson.objectid import ObjectId
from api.services.generic_service import GenericService

class UserPregnancyInfoService(GenericService):
    def __init__(self):
        super().__init__(UserPregnancyInfo.objects)
        
    def insert(self, obj):
        is_first_pregnancy = (obj['is_first_pregnancy'])
        is_planned_pregnancy = (obj['is_planned_pregnancy'])
        is_doing_pre_natal = (obj['is_doing_pre_natal'])
        last_menstruation_date = (obj['last_menstruation_date'])
        first_ultrasound_date = (obj['first_ultrasound_date'])
        
        user_pregnancy_info = UserPregnancyInfo(
                             is_first_pregnancy=is_first_pregnancy,
                             is_planned_pregnancy=is_planned_pregnancy,
                             is_doing_pre_natal=is_doing_pre_natal,
                             last_menstruation_date=last_menstruation_date,                             
                             first_ultrasound_date=first_ultrasound_date,
                             user_id=obj['user'].to_dbref())
        
        user_pregnancy_info.save()

    def get_by_user_id(self, user_id):
        return self.objects(Q(user_id=ObjectId(user_id))).first()

    def update(self, obj):
        user_pregnancy_info = self.get(obj['id'])

        if not user_pregnancy_info:
            raise Exception('Object with id {} not found!'.format(obj['id']))
        
        user_pregnancy_info.current_high_risk = (obj['current_high_risk'])
        user_pregnancy_info.due_date = (obj['due_date'])
        user_pregnancy_info.births = (obj['births'])
        user_pregnancy_info.cesarean_births = (obj['cesarean_births'])
        user_pregnancy_info.normal_births = (obj['normal_births'])
        user_pregnancy_info.why_cesarean_birth = (obj['why_cesarean_birth'])
        user_pregnancy_info.abortion = (obj['abortion'])
        user_pregnancy_info.premature_birth = (obj['premature_birth'])        
        
        user_pregnancy_info.save()