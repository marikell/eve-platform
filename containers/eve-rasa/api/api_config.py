class ApiConfig():
    def __init__(self):
        #has container name to localhost
        self.EVE_API = "http://eve_api:5001/api"
    @staticmethod
    def get_URL(self):
        return self.EVE_API
    @staticmethod
    def get_action_answer_URL(self):
        return self.get_URL() + "/action-answer"