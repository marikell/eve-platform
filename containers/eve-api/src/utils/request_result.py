from flask import jsonify
from enums.status_code_enum import StatusCode
from utils.mongo_encoder import jsonify as mjsonify

class RequestResult():
    def __init__(self):
        pass
    @staticmethod
    def response(status_code, success, message=''):
        return jsonify({'success':True, 'status_code': StatusCode.OK.value,'message':message})
    @staticmethod
    def response_content(data):
        return mjsonify(data)
