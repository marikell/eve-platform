class MongoConfig():
    def __init__(self, dbname, uri):
        self.mongo_dbName = dbname
        self.mongo_uri = uri

    def getConfig(self):
        return {"MONGO_DBNAME": self.mongo_dbName, "MONGO_URI": self.mongo_uri}