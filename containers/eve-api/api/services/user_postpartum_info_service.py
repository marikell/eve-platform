from mongoengine.queryset.visitor import Q
from api.models.user_postpartum_info import UserPostpartumInfo
from bson.objectid import ObjectId
from api.services.generic_service import GenericService

class UserPostpartumInfoService(GenericService):
    def __init__(self):
        super().__init__(UserPostpartumInfo.objects)
        
    def insert(self, obj):
        is_breastfeeding = (obj['is_breastfeeding'])
        is_having_sex = (obj['is_having_sex'])
        contraceptive_method = (obj['contraceptive_method'])
        had_doctor_appointment = (obj['had_doctor_appointment'])
        had_infection = (obj['had_infection'])
        infection_kind = (obj['infection_kind'])
        
        user_postpartum_info = UserPostpartumInfo(is_breastfeeding=is_breastfeeding, 
                             is_having_sex=is_having_sex,                             
                             contraceptive_method=contraceptive_method,
                             had_doctor_appointment=had_doctor_appointment, 
                             had_infection=had_infection,
                             infection_kind=infection_kind,
                             user_id=obj['user'].to_dbref())
        
        user_postpartum_info.save()

    def get_by_user_id(self, user_id):
        return self.objects(Q(user_id=ObjectId(user_id))).first()

    def update(self, obj):
        user_postpartum_info = self.get(obj['id'])

        if not user_postpartum_info:
            raise Exception('Object with id {} not found!'.format(obj['id']))

        user_postpartum_info.is_breastfeeding = (obj['is_breastfeeding'])
        user_postpartum_info.is_having_sex = (obj['is_having_sex'])
        user_postpartum_info.contraceptive_method = (obj['contraceptive_method'])
        user_postpartum_info.had_doctor_appointment = (obj['had_doctor_appointment'])
        user_postpartum_info.had_infection = (obj['had_infection'])
        user_postpartum_info.infection_kind = (obj['infection_kind'])
        
        user_postpartum_info.save()