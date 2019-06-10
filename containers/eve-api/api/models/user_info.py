from api.models.user import User
import datetime
from api.enums.user_enums import UserTypeEnum
from api.models.db_model import db

class UserInfo(db.DynamicDocument):
    is_first_pregnancy = db.BooleanField(required=False)
    has_children = db.BooleanField(required=False)
    has_health_plan = db.BooleanField(required=False),
    is_planning_with_doctor = db.BooleanField(required=False)
    is_pregnant = db.BooleanField(required=False)
    is_trying = db.BooleanField(required=False)
    is_planned_pregnancy = db.BooleanField(required=False)
    is_doing_pre_natal = db.BooleanField(required=False)
    user_id = db.ReferenceField(User, required=True)

    