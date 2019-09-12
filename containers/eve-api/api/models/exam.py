from api.models.db_model import db

class Exam(db.DynamicDocument):
    trimester = db.IntField(required=True)
    description = db.StringField(max_length=300, required=False)
    name = db.StringField(max_length=200, required=True)


    