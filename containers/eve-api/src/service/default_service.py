from config.mongo_config import MongoConfig as config
from flask_pymongo import PyMongo
from bson import json_util
import json

class DefaultService(object):
    def __init__(self, mongo):
        self.mongo = mongo

    def get_teste(self):
      testesDb = self.mongo.db.teste
      testes = []
      for t in testesDb.find():
        enc = json.dumps(t, default=json_util.default)
        testes.append(enc)
      return testes