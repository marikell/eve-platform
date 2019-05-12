from flask import Flask, jsonify, abort, make_response, request
from flask_pymongo import PyMongo
from service.default_service import DefaultService
from config.mongo_config import MongoConfig

app = Flask(__name__)


obj = MongoConfig()

# print(obj.getConfig()["MONGO_URI"])
app.config["MONGO_URI"] = obj.getConfig()["MONGO_URI"]
app.config["MONGO_DBNAME"] = obj.getConfig()["MONGO_DBNAME"]

mongo = PyMongo(app)

# print(mongo)

ds = DefaultService(mongo)

@app.route('/', methods=['GET'])
def get_hello_world():
    return jsonify('Flask is running in port 5001')

@app.route('/api/v1/messages', methods=['GET'])
def get_messages():   
    # print(list(ds.get_teste())
    # print(ds.get_teste())
    return jsonify(ds.get_teste())
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')