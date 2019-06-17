from api.models.user import User
from api.models.exam import Exam
import datetime
from api.enums.user_enums import UserTypeEnum
from api.models.db_model import db

class UserExam(db.DynamicDocument):
    exam_id = db.ReferenceField(Exam, required=True)
    user_id = db.ReferenceField(User, required=True)    

    