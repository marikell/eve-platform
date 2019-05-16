from mongoengine import connect
from config.database_config import DEV_MONGO_CONFIGURATION

class GenericService():
    def __init__(self):
        connect(DEV_MONGO_CONFIGURATION['DATABASE_NAME'], host=DEV_MONGO_CONFIGURATION['DATABASE_URL'])
    