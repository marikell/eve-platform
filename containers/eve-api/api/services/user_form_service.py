from mongoengine.queryset.visitor import Q
from api.models.user_form import UserForm
from bson.objectid import ObjectId
from api.services.generic_service import GenericService

class UserFormService(GenericService):
    def __init__(self):
        super().__init__(UserForm.objects)
        
    def insert(self, obj):
        user_form = UserForm(user_id=obj['user'].to_dbref(), form_id=obj['form'].to_dbref(), status=obj['status'])
        user_form.save()
        return user_form.id
    
    def get_user_form(self, user, form):
        return self.objects(Q(user_id=ObjectId(user.id), form_id=ObjectId(form.id))).first()
    
    def get(self, id):
        return self.objects(Q(id=ObjectId(id))).first()
    
    def update(self, obj):
        print(obj)
        user_form = self.get(obj['id'])

        if not user_form:
            raise Exception('Object with id {} not found!'.format(obj['id']))
        
        user_form.status = obj['status']
        user_form.save()

    def get_forms_by_user_status(self, user, status):
        return self.objects(Q(user_id=ObjectId(user), status=status)).first()

    def get_all_forms_by_user(self, userId):
        forms = UserForm.objects(Q(user_id=ObjectId(userId)))

        return forms
    
    def get_form_by_user(self, form, user):
        return self.objects(Q(user_id=ObjectId(user), form_id=ObjectId(form))).first()