from api.models.notification_user import NotificationUser
from api.services.generic_service import GenericService
from bson.objectid import ObjectId
from mongoengine.queryset.visitor import Q
import json

class NotificationUserService(GenericService):
    def __init__(self):
        super().__init__(NotificationUser.objects)  
 
    def get_all_by_user(self, user_id):
        notifications_user = NotificationUser.objects(Q(user_id=ObjectId(user_id))).order_by('creation_date')

        return notifications_user

    def delete_by_user(self, id):
        notifications_user = self.get_all_by_user(id)
        for obj in notifications_user:
            notification_id = json.loads(obj.to_json())['_id']['$oid']
            self.delete(notification_id)
            
    def insert(self, obj):        
        notification_user = NotificationUser(title=obj['title'],description=obj['description'], user_id=obj['user'].to_dbref())
        notification_user.save()
