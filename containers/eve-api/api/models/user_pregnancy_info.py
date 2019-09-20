from api.models.user import User
import datetime
from api.enums.user_enums import UserTypeEnum
from api.models.db_model import db
import dateutil.parser
from dateutil.relativedelta import relativedelta

class UserPregnancyInfo(db.DynamicDocument):
    is_first_pregnancy = db.BooleanField(required=False)
    is_planned_pregnancy = db.BooleanField(required=False)
    is_doing_pre_natal = db.BooleanField(required=False)
    last_menstruation_date = db.DateTimeField(required=False)
    first_ultrasound_date = db.DateTimeField(required=False)
    current_high_risk = db.BooleanField(required=False)
    due_date = db.DateTimeField(required=False)
    births = db.IntField(required=False)
    cesarean_births = db.IntField(required=False)
    normal_births = db.IntField(required=False)
    why_cesarean_birth = db.StringField(max_length=300, required=False)
    abortion = db.BooleanField(required=False)
    premature_birth = db.BooleanField(required=False)
    user_id = db.ReferenceField(User, required=True)

    def save(self, *args, **kwargs):
        if isinstance(self.last_menstruation_date, str):
            self.last_menstruation_date = dateutil.parser.parse(self.last_menstruation_date)
            if self.last_menstruation_date > datetime.datetime.now(self.last_menstruation_date.tzinfo):
                self.last_menstruation_date = self.last_menstruation_date - relativedelta(years=1)
        if isinstance(self.first_ultrasound_date, str):
            self.first_ultrasound_date = dateutil.parser.parse(self.first_ultrasound_date)
            if self.first_ultrasound_date > datetime.datetime.now(self.first_ultrasound_date.tzinfo):
                self.first_ultrasound_date = self.first_ultrasound_date - relativedelta(years=1)
        if isinstance(self.due_date, str):
            self.due_date = dateutil.parser.parse(self.due_date)
            if self.due_date > datetime.datetime.now(self.due_date.tzinfo):
                self.due_date = self.due_date - relativedelta(years=1)
        return super(UserPregnancyInfo, self).save(*args, **kwargs)
    