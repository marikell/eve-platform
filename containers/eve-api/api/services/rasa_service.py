from api.models.user_info import UserInfo
from api.services.generic_service import GenericService

class RasaService():
    def insert_initial_form_slots(self, obj):        
        user_info = UserInfo(is_first_pregnancy=obj['is_first_pregnancy'], 
                             has_children=obj['has_children'],
                             has_health_plan=obj['has_health_plan'], 
                             is_planning=obj['is_planning'],
                             is_pregnant=obj['is_pregnant'],
                             is_trying=obj['is_trying'],
                             is_planned_pregnancy=obj['is_planned_pregnancy'],
                             is_doing_pre_natal=obj['is_doing_pre_natal'],
                             last_menstruation_date=obj['last_menstruation_date'],
                             first_ultrasound_date=obj['first_ultrasound_date'],
                             user_id=obj['user'].to_dbref())        
        
        user_info.save()

        