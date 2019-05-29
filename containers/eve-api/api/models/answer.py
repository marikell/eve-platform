from api.models.db_model import db

class Answer(db.DynamicDocument):
    text = db.StringField(max_length=1000, required=True)
    