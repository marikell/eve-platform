from api.models.person import Person
import datetime
from api.enums.user_enums import UserTypeEnum
from api.models.db_model import db

class User(db.DynamicDocument):
    email = db.EmailField(required=True)
    password = db.StringField(max_length=300, required=True)
    creation_date = db.DateTimeField(required=True)
    user_type = db.IntField(required=True)
    person_id = db.ReferenceField(Person, required=True)
    is_admin = db.BooleanField(required=True)

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.datetime.now()
        return super(User, self).save(*args, **kwargs)

    