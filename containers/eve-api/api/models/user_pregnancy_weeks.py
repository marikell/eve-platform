from api.models.user import User
import datetime
from api.enums.user_enums import UserTypeEnum
from api.models.db_model import db

class UserPregnancyWeeks(db.DynamicDocument):
    weeks = db.IntField(required=True)
    weeks_start = db.IntField(required=True)
    creation_date = db.DateTimeField(required=True)
    user_id = db.ReferenceField(User, required=True)

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.datetime.now()
        return super(UserPregnancyWeeks, self).save(*args, **kwargs)

    