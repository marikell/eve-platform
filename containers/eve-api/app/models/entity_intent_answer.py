from mongoengine import *
from models.answer import Answer

class EntityIntentAnswer(DynamicDocument):
    entities = ListField(StringField(max_length=50), required=False)
    intent = StringField(max_length=100, required=True)
    answer_id = ReferenceField(Answer, required=True)

    