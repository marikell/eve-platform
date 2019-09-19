from api.models.answer import Answer
from api.models.db_model import db

class IntentAnswer(db.DynamicDocument):
    intent = db.StringField(max_length=100, required=True)
    answer_id = db.ReferenceField(Answer, required=True)

    