from api.models.user import User
from api.models.exam import Exam
import datetime
from api.models.db_model import db

class UserExam(db.DynamicDocument):
    exam_id = db.ReferenceField(Exam, required=True)
    user_id = db.ReferenceField(User, required=True)    
    exam_status = db.IntField(required=True)
    update_date = db.DateTimeField(required=False)

    def save(self, *args, **kwargs):
        self.update_date = datetime.datetime.now()
        return super(UserExam, self).save(*args, **kwargs)

    