from api.models.user import User
import datetime
from api.enums.user_enums import UserTypeEnum
from api.models.db_model import db
import dateutil.parser
from dateutil.relativedelta import relativedelta

class UserInfo(db.DynamicDocument):
    has_children = db.BooleanField(required=False)
    has_health_plan = db.BooleanField(required=False)
    is_planning_with_doctor = db.BooleanField(required=False)
    is_pregnant = db.BooleanField(required=False)
    is_trying = db.BooleanField(required=False)
    is_postpartum = db.BooleanField(required=False)
    height = db.FloatField(required=False)
    weight = db.FloatField(required=False)
    state = db.StringField(max_length=45, required=False)
    user_id = db.ReferenceField(User, required=True)
