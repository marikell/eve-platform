import datetime
from api.enums.user_enums import UserTypeEnum
from api.models.db_model import db

class User(db.DynamicDocument):
    name = db.StringField(max_length=300)    
    email = db.EmailField(required=True)
    password = db.StringField(max_length=300, required=True)
    creation_date = db.DateTimeField(required=True)
    name = db.StringField(max_length=300)
    date_birth = db.DateTimeField(required=False)
    user_type = db.IntField(required=True)
    accepts_notifications = db.BooleanField(required=True)



    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.datetime.now()
        return super(User, self).save(*args, **kwargs)

    