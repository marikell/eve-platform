from mongoengine import *
from answer import Answer

class IntentAnswer(DynamicDocument):
    intent = StringField(max_length=100, required=True)
    answer_id = ReferenceField(Answer, required=True)