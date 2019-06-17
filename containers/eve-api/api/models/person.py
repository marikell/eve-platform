from api.models.db_model import db

class Person(db.DynamicDocument):
    name = db.StringField(max_length=300)
    date_birth = db.DateTimeField(required=False)