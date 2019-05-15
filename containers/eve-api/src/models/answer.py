from mongoengine import *

class Answer(DynamicDocument):
    text = StringField(max_length=1000, required=True)
    