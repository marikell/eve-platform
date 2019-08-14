from api.models.user import User
import datetime
from api.enums.user_enums import UserTypeEnum
from api.models.db_model import db
import dateutil.parser
from dateutil.relativedelta import relativedelta

class UserTrimester(db.DynamicDocument):
    update_date = db.DateTimeField(required=False)
    start_date = db.DateTimeField(required=True)
    trimester = db.IntField(required=False)
    user_id = db.ReferenceField(User, required=True)

    def save(self, *args, **kwargs):
        self.update_date = datetime.datetime.now()
        return super(UserTrimester, self).save(*args, **kwargs)
    