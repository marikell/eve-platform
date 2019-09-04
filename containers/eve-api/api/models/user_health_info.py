from api.models.user import User
import datetime
from api.enums.user_enums import UserTypeEnum
from api.models.db_model import db
import dateutil.parser
from dateutil.relativedelta import relativedelta

class UserHealthInfo(db.DynamicDocument):
    takes_regular_medicine = db.BooleanField(required=False)
    regular_medicine_name = db.StringField(required=False)
    has_hypothyroidism = db.BooleanField(required=False)
    has_hyperthyroidism = db.BooleanField(required=False)
    has_diabetes = db.BooleanField(required=False)
    drug_use = db.BooleanField(required=False)
    has_autoimmune_disease = db.BooleanField(required=False)
    has_asthma = db.BooleanField(required=False)
    is_seropositive = db.BooleanField(required=False)
    has_high_pressure = db.BooleanField(required=False)
    user_id = db.ReferenceField(User, required=True)
