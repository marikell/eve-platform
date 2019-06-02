from mongoengine.queryset.visitor import Q
from api.models.person import Person
from api.services.generic_service import GenericService

class PersonService(GenericService):
    def __init__(self):
        super().__init__(Person.objects)     
    
    def insert(self, obj):
        person = Person(name=obj['name'])
        person.save()

        return person

    def update(self, obj):
        person = self.get(obj['id'])

        if not person:
            raise Exception('Object with id {} not found!'.format(obj['id']))

        person.name = obj['name']
        person.save()