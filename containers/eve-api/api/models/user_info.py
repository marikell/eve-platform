from api.models.user import User
import datetime
from api.enums.user_enums import UserTypeEnum
from api.models.db_model import db
import dateutil.parser
from dateutil.relativedelta import relativedelta

class UserInfo(db.DynamicDocument):
    is_first_pregnancy = db.BooleanField(required=False)
    has_children = db.BooleanField(required=False)
    has_health_plan = db.BooleanField(required=False),
    is_planning_with_doctor = db.BooleanField(required=False)
    is_pregnant = db.BooleanField(required=False)
    is_trying = db.BooleanField(required=False)
    is_planned_pregnancy = db.BooleanField(required=False)
    is_doing_pre_natal = db.BooleanField(required=False)
    last_menstruation_date = db.DateTimeField(required=False)
    first_ultrasound_date = db.DateTimeField(required=False)
    user_id = db.ReferenceField(User, required=True)

    def save(self, *args, **kwargs):
        if self.last_menstruation_date:            
            self.last_menstruation_date = dateutil.parser.parse(self.last_menstruation_date)
            if self.last_menstruation_date > datetime.datetime.now(self.last_menstruation_date.tzinfo):
                self.last_menstruation_date = self.last_menstruation_date - relativedelta(years=1)
        if self.first_ultrasound_date:
            self.first_ultrasound_date = dateutil.parser.parse(self.first_ultrasound_date)
            if self.first_ultrasound_date > datetime.datetime.now(self.first_ultrasound_date.tzinfo):
                self.first_ultrasound_date = self.first_ultrasound_date - relativedelta(years=1)
        return super(UserInfo, self).save(*args, **kwargs)

    