from api.models.db_model import db

class FollowUp(db.DynamicDocument):
    weeks_start = db.IntField(required=True)
    weeks_end = db.IntField(required=False)
    description = db.StringField(max_length=300, required=False)
    name = db.StringField(max_length=200, required=True)
    followup_type = db.IntField(required=True)

    