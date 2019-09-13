from api.models.user import User
from api.models.form import Form
import datetime
from api.models.db_model import db

class UserForm(db.DynamicDocument):
    form_id = db.ReferenceField(Form, required=True)
    user_id = db.ReferenceField(User, required=True)
    status = db.IntField(required=True)
    