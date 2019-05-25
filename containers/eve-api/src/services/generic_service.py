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

    def get(self, id:str):
        obj = self.objects.get(Q(_id=ObjectId(id)))
        return obj
    