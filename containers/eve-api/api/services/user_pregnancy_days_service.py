from mongoengine.queryset.visitor import Q
from api.models.user_pregnancy_days import UserPregnancyDays
from bson.objectid import ObjectId  
from api.services.generic_service import GenericService

class UserPregnancyDaysService(GenericService):
    def __init__(self):
        super().__init__(UserPregnancyDays.objects)
        
    def insert(self, obj):
        user_pregnancy_days = UserPregnancyDays(days=obj['days'], user_id=obj['user'].to_dbref(),
        days_start=obj['days_start'])
        user_pregnancy_days.save()

    def get_by_user(self, user):
        return self.objects(Q(user_id=ObjectId(user.id))).first()

    def update(self, obj):
        user_pregnancy_days = self.get(obj['id'])

        if not user_pregnancy_days:
            raise Exception('Object with id {} not found!'.format(obj['id']))
        
        user_pregnancy_days.days = obj['days']

        user_pregnancy_days.save()