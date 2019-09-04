from api.models.user import User
import datetime
from api.enums.user_enums import UserTypeEnum
from api.models.db_model import db
import dateutil.parser
from dateutil.relativedelta import relativedelta

class UserPostpartumInfo(db.DynamicDocument):
    is_breastfeeding = db.BooleanField(required=False)
    is_having_sex = db.BooleanField(required=False)
    contraceptive_method = db.StringField(max_length=100, required=False)
    had_doctor_appointment = db.BooleanField(required=False)
    had_infection = db.BooleanField(required=False)
    infection_kind = db.StringField(max_length=100, required=False)
    user_id = db.ReferenceField(User, required=True)
