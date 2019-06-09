from api.models.db_model import db

class Conversations(db.DynamicDocument):
    sender_id = db.StringField(max_length=300)
