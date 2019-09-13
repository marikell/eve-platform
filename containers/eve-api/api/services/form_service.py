from api.models.form import Form
from api.services.generic_service import GenericService
from mongoengine.queryset.visitor import Q

class FormService(GenericService):
    def __init__(self):
        super().__init__(Form.objects)        

    def insert(self, obj):        
        form = Form(name=obj['name'])
        form.save()

    def get_by_name(self, form_name):
        return self.objects(Q(name=form_name)).first()