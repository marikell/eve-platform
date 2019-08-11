from mongoengine.queryset.visitor import Q
from api.models.user_pregnancy_info import UserPregnancyInfo
from bson.objectid import ObjectId
from api.services.generic_service import GenericService

class UserPregnancyInfoService(GenericService):
    def __init__(self):
        super().__init__(UserPregnancyInfo.objects)
        
    def insert(self, obj):                                        
        
        current_high_risk = (obj['current_high_risk'])
        due_date = (obj['due_date'])
        births = (obj['births'])
        cesarean_births = (obj['cesarean_births'])
        normal_births = (obj['normal_births'])
        why_cesarean_birth = (obj['why_cesarean_birth'])
        abortion = (obj['abortion'])
        premature_birth = (obj['premature_birth'])        
        
        user_pregnancy_info = UserPregnancyInfo(current_high_risk=current_high_risk, 
                             due_date=due_date,                             
                             births=births,
                             cesarean_births=cesarean_births, 
                             normal_births=normal_births,
                             why_cesarean_birth=why_cesarean_birth,
                             abortion=abortion,
                             premature_birth=premature_birth,
                             user_id=obj['user'].to_dbref())
        
        user_pregnancy_info.save()


    def get_by_user(self, user):
        return self.objects(Q(user_id=ObjectId(user.id))).first()

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