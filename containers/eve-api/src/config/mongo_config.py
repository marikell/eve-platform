class MongoConfig():
    def __init__(self):
        self.mongo_dbName = 'eveDb'
        self.mongo_uri = 'mongodb://eve_mongo:27017/eveDb'

    def getConfig(self):
        return {"MONGO_DBNAME": self.mongo_dbName, "MONGO_URI": self.mongo_uri}