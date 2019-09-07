from mongoengine.queryset.visitor import Q
from api.models.user import User
from api.services.generic_service import GenericService

class UserService(GenericService):
    def __init__(self):
        super().__init__(User.objects)        

    def insert(self, obj):        
        user = User(email=obj['email'], 
        password=obj['password'],name=obj['name'],user_type=obj['user_type'], date_birth=obj['birthDate'], accepts_notifications=obj['accepts_notifications'])        

        if User.objects(email=obj['email']):
            raise Exception('Esse e-mail já foi cadastrado.')
        
        user.save()
    
    def change_password(self, new_password, user):
        user.password = new_password
        user.save()


    def getby_email(self, email):
        return User.objects(Q(email=email)).first()

    def update_user_type(self, id, user_type):
        user = self.get(id)

        if not user:
            raise Exception('Object with id {} not found!'.format(id))

        user.user_type = user_type
        user.save()

    
    def update_accepts_notifications(self, id, accepts_notification):
        user = self.get(id)

        if not user:
            raise Exception('Object with id {} not found!'.format(id))

        user.accepts_notifications = accepts_notification
        user.save()   

    def update(self, obj):
        user = self.get(obj['id'])

        if not user:
            raise Exception('Object with id {} not found!'.format(obj['id']))
        
        user.email = obj['email']
        user.password = obj['password']
        user.is_admin = obj['is_admin']
        user.user_type = obj['user_type']

        user.save()