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
        
    def get_user_pregnancy_weeks(self,user_id):
        r = requests.get(url = '{}/user-pregnancy-weeks/{}'.format(EVE_API['url'], user_id))

        json_obj = r.json()

        if json_obj['status'] == 400:
            get_log(json_obj['response'])
            return

        obj = json.loads(json_obj['response'])
        return obj

            
    def update_user_pregnancy_weeks(self, obj):
        #increasing user weeks of pregnancy
        data = {
            "weeks": (int(obj['weeks']) + 1)
        }

        headers = {
            'Content-Type':'application/json'
        }
        url = '{}/user-pregnancy-weeks/{}'.format(EVE_API['url'], obj['_id']['$oid'])

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

            user_pregnancy_weeks = self.get_user_pregnancy_weeks(user_id)

            get_log('User {} is pregnant with {} weeks.'.format(user_id, user_pregnancy_weeks['weeks']))
            
            self.update_user_pregnancy_weeks(user_pregnancy_weeks)

            get_log('Successfully updated user {} weeks.'.format(user_id))        

        except Exception as e:
            get_log(str(e))
        finally:
            get_log('Finished User Job for {}'.format(user_id))