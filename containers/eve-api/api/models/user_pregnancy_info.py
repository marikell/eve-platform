from api.models.user import User
import datetime
from api.enums.user_enums import UserTypeEnum
from api.models.db_model import db
import dateutil.parser
from dateutil.relativedelta import relativedelta

class UserPregnancyInfo(db.DynamicDocument):
    current_high_risk = db.BooleanField(required=False)
    due_date = db.DateTimeField(required=False)
    births = db.IntField(required=False)
    cesarean_births = db.IntField(required=False)
    normal_births = db.IntField(required=False)
    why_cesarean_birth = db.StringField(max_length=300, required=False)
    abortion = db.BooleanField(required=False)
    premature_birth = db.BooleanField(required=False)
    user_id = db.ReferenceField(User, required=True)
    