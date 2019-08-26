from config.configuration import EVE_API
from enums.enums import TipTypeEnum
import requests
import json
import traceback
from datetime import datetime
from datetime import date


class NotifyJob():
    def get_tip_by_type(self, tip_type):
        headers = {
            'Content-Type': 'application/json'
        }
        json_data = {
            'tip_type': tip_type
        }

        req = requests.post(url='{}/tip/filtered-tip'.format(
            EVE_API['url']), headers=headers, data=json.dumps(json_data))

        json_obj = req.json()

        if json_obj['status'] == 400:
            return None
        return json.loads(json_obj['response'])['description']

    def get_all_users_infos(self):
        r = requests.get(url='{}/notify/users-info'.format(EVE_API['url']))
        json_obj = r.json()

        if json_obj['status'] == 400:
            return None

        join_response = json.loads(json_obj['response'])
        return join_response

    def notify(self, emails, tip):
        header = {"Content-Type": "application/json; charset=utf-8",
                  "Authorization": "Basic MDhjNzVmMTAtYzVhZC00MWM4LWJmMWMtMDg0ZDk4NWY4NDQ2"}

        payload = {"app_id": "62f0fa9f-3e8e-4514-92bb-a718d2600362",
                   "include_email_tokens": emails,
                   "contents": {"en": tip}}

        req = requests.post("https://onesignal.com/api/v1/notifications", headers=header, data=json.dumps(payload))
        print(req.json())

    def reset(self, tip_type):
        return
        # deve resetar todas as dicas de determinado tipo

    def run(self):
        users_info = self.get_all_users_infos()
        pregnant_users = []
        is_trying_users = []
        not_categorized_users = []

        pregnant_tip = self.get_tip_by_type(TipTypeEnum.pregnant)
        trying_tip = self.get_tip_by_type(TipTypeEnum.wanting_conceive)
        after_birth_tip = self.get_tip_by_type(TipTypeEnum.after_birth)

        if(not pregnant_tip):
            print('uhasuhas')
            # reset

        if(not trying_tip):
            print('uhasuhas')
            # reset

        if(not after_birth_tip):
            print('uhasuhas')
            # reset

        for usi in users_info:
            if len(list(usi['user_infos'])) > 0:
                user_info = list(usi['user_infos'])[0]
                print(user_info)
                if 'is_pregnant' in user_info:
                    print('is_pregnant')
                    pregnant_users.append(usi['email'])
                elif 'is_trying' in user_info:
                    print('is_trying')
                    is_trying_users.append(usi['email'])
                else:
                    not_categorized_users.append(usi['email'])
            else:
                not_categorized_users.append(usi['email'])


NotifyJob().run()
