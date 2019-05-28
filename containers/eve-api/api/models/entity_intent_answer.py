from api.models.answer import Answer
from api.models.db_model import db

class EntityIntentAnswer(db.DynamicDocument):
    entities = db.ListField(db.StringField(max_length=50), required=False)
    intent = db.StringField(max_length=100, required=True)
    answer_id = db.ReferenceField(Answer, required=True)

    