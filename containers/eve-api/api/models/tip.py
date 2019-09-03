import datetime
from api.models.db_model import db

class Tip(db.DynamicDocument):
    description = db.StringField(max_length=1000)    
    send = db.BooleanField(required=True)
    tip_type = db.IntField(required=True)