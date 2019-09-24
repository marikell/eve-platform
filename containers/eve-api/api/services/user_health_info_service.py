from mongoengine.queryset.visitor import Q
from api.models.user_health_info import UserHealthInfo
from bson.objectid import ObjectId
from api.services.generic_service import GenericService

class UserHealthInfoService(GenericService):
    def __init__(self):
        super().__init__(UserHealthInfo.objects)
        
    def insert(self, obj):
        
        takes_regular_medicine = (obj['takes_regular_medicine'])
        regular_medicine_name = (obj['regular_medicine_name'])
        has_hypothyroidism = (obj['has_hypothyroidism'])
        has_hyperthyroidism = (obj['has_hyperthyroidism'])
        has_diabetes = (obj['has_diabetes'])
        drug_use = (obj['drug_use'])
        has_autoimmune_disease = (obj['has_autoimmune_disease'])
        has_asthma = (obj['has_asthma'])
        is_seropositive = (obj['is_seropositive'])
        has_high_pressure = (obj['has_high_pressure'])
        
        user_health_info = UserHealthInfo(takes_regular_medicine=takes_regular_medicine, 
                             regular_medicine_name=regular_medicine_name,                             
                             has_hypothyroidism=has_hypothyroidism,
                             has_hyperthyroidism=has_hyperthyroidism, 
                             has_diabetes=has_diabetes,
                             drug_use=drug_use,
                             has_autoimmune_disease=has_autoimmune_disease,
                             has_asthma=has_asthma,
                             is_seropositive=is_seropositive,
                             has_high_pressure=has_high_pressure,
                             user_id=obj['user'].to_dbref())
        
        user_health_info.save()


    def get_by_user_id(self, id):
        return self.objects(Q(user_id=ObjectId(id))).first()

    def update(self, obj):
        user_health_info = self.get(obj['id'])

        if not user_health_info:
            raise Exception('Object with id {} not found!'.format(obj['id']))
        
        user_health_info.takes_regular_medicine = (obj['takes_regular_medicine'])
        user_health_info.regular_medicine_name = (obj['regular_medicine_name'])
        user_health_info.has_hypothyroidism = (obj['has_hypothyroidism'])
        user_health_info.has_hyperthyroidism = (obj['has_hyperthyroidism'])
        user_health_info.has_diabetes = (obj['has_diabetes'])
        user_health_info.drug_use = (obj['drug_use'])
        user_health_info.has_autoimmune_disease = (obj['has_autoimmune_disease'])
        user_health_info.has_asthma = (obj['has_asthma'])
        user_health_info.is_seropositive = (obj['is_seropositive'])
        user_health_info.has_high_pressure = (obj['has_high_pressure'])

        user_health_info.save()