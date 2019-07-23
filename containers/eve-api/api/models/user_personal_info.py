from api.models.user import User
import datetime
from api.enums.user_enums import UserTypeEnum
from api.models.db_model import db
import dateutil.parser
from dateutil.relativedelta import relativedelta

class UserPersonalInfo(db.DynamicDocument):
    height = db.FloatField(required=False)
    weight = db.FloatField(required=False)
    date_birth = db.DateTimeField(required=False)
    state = db.StringField(max_length=45, required=False)
    user_id = db.ReferenceField(User, required=True)
    
    