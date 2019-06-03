from mongoengine.queryset.visitor import Q
from api.models.user_weeks import UserWeeks
from api.services.generic_service import GenericService

class UserWeeksService(GenericService):
    def __init__(self):
        super().__init__(UserWeeks.objects)     
    
    def insert(self, obj):
        user_week = UserWeeks(weeks=obj['weeks'], user_id=obj['user'].to_dbref())
        user_week.save()

    def get_most_recently_record(self, id):
        obj = self.objects(Q(_id=ObjectId(id)))
        self.objects..order_by('-creation_date').first()