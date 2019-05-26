from mongoengine import connect
from mongoengine import QuerySetManager
from utils.config_json import read_json
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