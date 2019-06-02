from api.models.person import Person
from api.enums.user_enums import UserTypeEnum
from api.models.db_model import db

class User(db.DynamicDocument):
    email = db.EmailField(required=True)
    password = db.StringField(max_length=300, required=True)
    user_type = db.IntField(required=True)
    person_id = db.ReferenceField(Person, required=True)
    is_admin = db.BooleanField(required=True)

    