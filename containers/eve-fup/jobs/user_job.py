from config.configuration import EVE_API
import requests 
from helpers.logging import get_log
from enums.service_enums import UserTypeEnum
import json
import traceback
from datetime import datetime
from datetime import date

class UserJob():
    def run(self):
        r = requests.get(url = '{}/user'.format(EVE_API['url']))
        users = list(json.loads(r.text)['response'])

        get_log('Users to process: {}'.format(len(users)))
        [self.execute_job(usr) for usr in users]
        
    def get_user_pregnancy_trimester(self,user_id):
        r = requests.get(url = '{}/user-trimester/{}'.format(EVE_API['url'], user_id))

        json_obj = r.json()

        if json_obj['status'] == 400:
            get_log(json_obj['response'])
            return

        obj = json.loads(json_obj['response'])
        return obj

            
    def update_user_pregnancy_trimester(self, obj):
        #increasing user trimester of pregnancy
        data = {
            "trimester": (int(obj['trimester']) + 1)
        }

        headers = {
            'Content-Type':'application/json'
        }
        url = '{}/user-trimester/{}'.format(EVE_API['url'], obj['_id']['$oid'])

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

            user_trimester = self.get_user_pregnancy_trimester(user_id)            
            update_date = user_trimester['update_date']['$date']
            today = date.today()            
            trimester = user_trimester['trimester']
            
            update_date = date.fromtimestamp(update_date/1000)
            date_diff = today - update_date            
            
            if(date_diff.days >= 90 and trimester < 3):
                r = requests.get(url = '{}/user'.format(EVE_API['url']))
                get_log('User {} is pregnant in {} trimester.'.format(user_id, user_trimester['trimester']))
            
                self.update_user_pregnancy_trimester(user_trimester)

                get_log('Successfully updated user {} trimester.'.format(user_id))        

        except Exception as e:
            get_log(str(e))
        finally:
            get_log('Finished User Job for {}'.format(user_id))
