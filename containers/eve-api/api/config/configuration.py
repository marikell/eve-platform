MONGO_CONFIG:dict = {
    'db' : 'evedb',
    'host' : 'mongodb://eve_mongo:27017/evedb'
}

API_SECRET_KEY = 'evesecretkey'

ROUTE_CONFIG:dict = {
    'ANSWER_TYPE_NAME':'answer',
    'INTENT_ANSWER_TYPE_NAME':'intent-answer',
    'USER_TYPE_NAME':'user',
    'EXAM_TYPE_NAME':'exam',
    'USER_INFO_TYPE_NAME':'user-info',
    'USER_EXAM_TYPE_NAME':'user-exam',
    'USER_HEALTH_INFO_TYPE_NAME':'user-health',
    'USER_PREGNANCY_INFO_TYPE_NAME':'user-pregnancy',
    'USER_POSTPARTUM_INFO_TYPE_NAME':'user-postpartum',
    'USER_PERSONAL_INFO_TYPE_NAME':'user-personal',
    'USER_TRIMESTER_TYPE_NAME':'user-trimester',
    'UNANSWERED_QUESTION_TYPE_NAME':'unanswered-question',
    'NOTIFICATION_USER_TYPE_NAME':'notification-user',
    'FORM_TYPE_NAME':'form',
    'USER_FORM_TYPE_NAME':'user-form',
    'TIP_TYPE_NAME':'tip',
    'CONVERSATIONS_TYPE_NAME': 'conversations',
    'FUP':'fup',
    'NOTIFY':'notify',
    'RASA' : 'rasa'
}

