from config.mongo_config import MongoConfig as config
from flask_pymongo import PyMongo
from bson import json_util
from util import mongo_encoder as MongoEncoder
import json

class DefaultService(object):
    def __init__(self, mongo):
        self.mongo = mongo

    def get_teste(self):
        return [t for t in self.mongo.db.teste.find()]