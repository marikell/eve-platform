from mongoengine import *

class Answer(Document):
    text = StringField(max_length=2000, required=True)