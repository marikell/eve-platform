import datetime
from api.models.user import User
from api.models.db_model import db

class NotificationUser(db.DynamicDocument):
    description = db.StringField(max_length=1000)    
    user_id = db.ReferenceField(User, required=True)
    creation_date = db.DateTimeField(required=True)

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.datetime.now()

        return super(NotificationUser, self).save(*args, **kwargs)