from api.models.follow_up import FollowUp
from api.services.generic_service import GenericService

class FollowUpService(GenericService):
    def __init__(self):
        super().__init__(FollowUp.objects)        

    def insert(self, obj):        
        followup = FollowUp(weeks_start=obj['weeks_start'], weeks_end=obj['weeks_end'],description=obj['description'], 
        name=obj['name'],followup_type=obj['followup_type'])        
        
        followup.save()