from api.models.user import User
import datetime
from api.enums.user_enums import UserTypeEnum
from api.models.db_model import db

class UserPregnancyDays(db.DynamicDocument):
    days = db.IntField(required=True)
    days_start = db.IntField(required=True)
    creation_date = db.DateTimeField(required=True)
    user_id = db.ReferenceField(User, required=True)

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.datetime.now()
        return super(UserPregnancyDays, self).save(*args, **kwargs)

    