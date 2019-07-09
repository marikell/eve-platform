MONGO_CONFIG:dict = {
    'db' : 'evedb',
    'host' : 'mongodb://eve_mongo:27017/evedb'
}

ROUTE_CONFIG:dict = {
    'ANSWER_TYPE_NAME':'answer',
    'ENTITY_INTENT_ANSWER_TYPE_NAME':'entity-intent-answer',
    'USER_TYPE_NAME':'user',
    'EXAM_TYPE_NAME':'exam',
    'USER_INFO_TYPE_NAME':'user-info',
    'USER_EXAM_TYPE_NAME':'user-exam',
    'USER_HEALTH_INFO_TYPE_NAME':'user-health',
    #this endpoint will be called by the fup service
    'FUP':'fup',
    #this endpoint will be called by rasa to send data
    'RASA' : 'rasa'
}

