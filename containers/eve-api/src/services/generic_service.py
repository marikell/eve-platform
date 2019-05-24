from mongoengine import connect
from config.database_config import PROD_MONGO_CONFIGURATION

class GenericService():
    def __init__(self):
        connect(PROD_MONGO_CONFIGURATION['DATABASE_NAME'], host=PROD_MONGO_CONFIGURATION['DATABASE_URL'])
    