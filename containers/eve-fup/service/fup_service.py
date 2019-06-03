from config.configuration import EVE_API
import requests 
from helpers.logging import get_log
from enums.service_enums import UserTypeEnum
from helpers.threading_schedule import run_threaded
import json

def get_all_users():
    r = requests.get(url = '{}/user'.format(EVE_API['url']))
    users = list(json.loads(r.text)['response'])

    get_log('Users to process: {}'.format(len(users)))
    [user_job(usr) for usr in users]
    
def check_user_weeks(id):
    r = requests.get(url = '{}/user/recent-weeks/{}'.format(EVE_API['url'], id))

    json_obj = r.json()

    if json_obj['status'] == 400:
        get_log(str(r.json()['response']))
        return

    print(r.json())
        
def update_user_weeks(user):
    print('Not implemented!')

def user_job(user):
    try:
        user_id = user['_id']['$oid']
        get_log('Starting User Job for {}'.format(user_id))

        if user['user_type'] != UserTypeEnum.pregnant.value:
            raise Exception('User {} will not be monitored!'.format(user_id))

        get_log('User {} is pregnant.'.format(user_id))

        check_user_weeks(user_id)

    except Exception as e:
        get_log(str(e))
    finally:
        get_log('Finished User Job for {}'.format(user_id))
    #Busco a data do user_weeks mais recente de determinada grávida. Se já contabilizou uma semana,
    #adiciono uma linha na tabela de user_weeks com as semanas incrementadas.
    

def routine():
    #checking users in routine
    get_all_users()