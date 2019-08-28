from api.models.tip import Tip
from api.services.generic_service import GenericService
from mongoengine.queryset.visitor import Q
import json

class TipService(GenericService):
    def __init__(self):
        super().__init__(Tip.objects)        

    def insert(self, obj):        
        tip = Tip(description=obj['description'], tip_type=obj['tip_type'], send=False)
        tip.save()

    def getby_type(self, tip_type):
        return Tip.objects((Q(tip_type=tip_type) & Q(send=False))).first()
    
    def reset_by_type(self, tip_type):
        items = Tip.objects(Q(tip_type=tip_type))
        for obj in items:
            obj.send = False
            obj.save()

    def update(self, obj):
        tip = self.get(obj['id'])

        if not tip:
            raise Exception('Object with id {} not found!'.format(obj['id']))

        tip.send = obj['send']
        tip.save()