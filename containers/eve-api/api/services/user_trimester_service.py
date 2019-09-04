from mongoengine.queryset.visitor import Q
from api.models.user_trimester import UserTrimester
from bson.objectid import ObjectId
from api.services.generic_service import GenericService

class UserTrimesterService(GenericService):
    def __init__(self):
        super().__init__(UserTrimester.objects)
        
    def insert(self, obj):
        trimester = (obj['trimester'])
        start_date = (obj['start_date'])
        
        user_trimester = UserTrimester(trimester=trimester,
                            start_date=start_date,
                             user_id=obj['user'].to_dbref())        
        user_trimester.save()


    def get_by_user_id(self, user_id):
        return self.objects(Q(user_id=ObjectId(user_id))).first()

    def update(self, obj):
        user_trimester = self.get(obj['id'])

        if not user_trimester:
            raise Exception('Object with id {} not found!'.format(obj['id']))
        
        user_trimester.trimester = (obj['trimester'])
        
        user_trimester.save()