from config.configuration import EVE_API
import requests 
from helpers.logging import get_log
from enums.service_enums import UserTypeEnum
import json
import traceback

class UserJob():
    def run(self):
        r = requests.get(url = '{}/user'.format(EVE_API['url']))
        users = list(json.loads(r.text)['response'])

        get_log('Users to process: {}'.format(len(users)))
        [self.execute_job(usr) for usr in users]
        
    def get_user_pregnancy_days(self,user_id):
        r = requests.get(url = '{}/user-pregnancy-days/{}'.format(EVE_API['url'], user_id))

        json_obj = r.json()

        if json_obj['status'] == 400:
            get_log(json_obj['response'])
            return

        obj = json.loads(json_obj['response'])
        return obj

            
    def update_user_pregnancy_days(self, obj):
        #increasing user weeks of pregnancy
        data = {
            "days": (int(obj['days']) + 1)
        }

        headers = {
            'Content-Type':'application/json'
        }
        url = '{}/user-pregnancy-days/{}'.format(EVE_API['url'], obj['_id']['$oid'])

        r = requests.put(url, data=json.dumps(data), headers=headers)

        json_obj = r.json()

        if json_obj['status'] == 400:
            get_log(json_obj['response'])
            return

    def execute_job(self,user):
        try:
            user_id = user['_id']['$oid']
            get_log('Starting User Job for {}'.format(user_id))

            if user['user_type'] != UserTypeEnum.pregnant.value:
                raise Exception('User {} will not be monitored!'.format(user_id))

            user_pregnancy_days = self.get_user_pregnancy_days(user_id)

            get_log('User {} is pregnant with {} weeks.'.format(user_id, user_pregnancy_days['days']/7))
            
            self.update_user_pregnancy_days(user_pregnancy_days)

            get_log('Successfully updated user {} weeks.'.format(user_id))        

        except Exception as e:
            traceback.print_exc()
            get_log(str(e))
        finally:
            get_log('Finished User Job for {}'.format(user_id))
        #Busco a data do user_weeks mais recente de determinada grávida. Se já contabilizou uma semana,
        #adiciono uma linha na tabela de user_weeks com as semanas incrementadas.