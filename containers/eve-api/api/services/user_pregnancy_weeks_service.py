from mongoengine.queryset.visitor import Q
from api.models.user_pregnancy_weeks import UserPregnancyWeeks
from bson.objectid import ObjectId  
from api.services.generic_service import GenericService

class UserPregnancyWeeksService(GenericService):
    def __init__(self):
        super().__init__(UserPregnancyWeeks.objects)
        
    def insert(self, obj):
        user_pregnancy_weeks = UserPregnancyWeeks(weeks=obj['weeks'], user_id=obj['user'].to_dbref(),
        weeks_start=obj['weeks_start'])
        user_pregnancy_weeks.save()

    # def get_pregnancy_weeks_by_exam(self, exam):
    #     return self.objects()

    def get_by_user(self, user):
        return self.objects(Q(user_id=ObjectId(user.id))).first()

    def update(self, obj):
        user_pregnancy_weeks = self.get(obj['id'])

        if not user_pregnancy_weeks:
            raise Exception('Object with id {} not found!'.format(obj['id']))
        
        user_pregnancy_weeks.weeks = obj['weeks']

        user_pregnancy_weeks.save()