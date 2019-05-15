from mongoengine import connect
from config.mongo_config import MongoConfig

class GenericService():
    def __init__(self):
        config = MongoConfig('eveDb','mongodb://eve_mongo:27017/eveDb')
        connect(config.getConfig()["MONGO_DBNAME"], host=config.getConfig()["MONGO_URI"])
    