configs:dict = {
    'ANSWER_TYPE_NAME' : 'answer',
    'ENTITY_INTENT_ANSWER_TYPE_NAME' : 'entity-intent-answer'
}

class RouteConfig():
    @staticmethod
    def get(name: str):
        return configs[name]
