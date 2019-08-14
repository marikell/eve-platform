from api.models.exam import Exam
from api.models.db_model import db

class Form(db.DynamicDocument):
    trimester = db.IntField(required=True)
    name = db.StringField(max_length=100, required=True)
