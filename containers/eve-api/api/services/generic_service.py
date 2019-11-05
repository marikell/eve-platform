import json
from mongoengine import connect
from mongoengine import QuerySetManager
from bson.objectid import ObjectId
from mongoengine.queryset.visitor import Q

class GenericService():   

    def __init__(self, objects):
        self.objects = objects
    
    def get_all(self):
        return self.objects

    def get(self, id):
        obj = self.objects(Q(_id=ObjectId(id))).first()
        return obj
    def delete(self, id):
        obj = self.get(id)
        if not obj:
            raise Exception('Object with id {} not found!'.format(id))
        obj.delete()

    def delete_by_user_id(self, user_id):
        senders = self.objects(Q(user_id=ObjectId(user_id)))
        for obj in senders:
            sender_id = json.loads(obj.to_json())['_id']['$oid']
            self.delete(sender_id)