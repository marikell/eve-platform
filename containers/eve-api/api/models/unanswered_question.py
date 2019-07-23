import datetime
from api.enums.user_enums import UserTypeEnum
from api.models.db_model import db

class UnansweredQuestion(db.DynamicDocument):
    question = db.StringField(max_length=300)    
    date = db.DateTimeField(required=False)

    def save(self, *args, **kwargs):
        if not self.date:
            self.date = datetime.datetime.now()
        return super(UnansweredQuestion, self).save(*args, **kwargs)

    