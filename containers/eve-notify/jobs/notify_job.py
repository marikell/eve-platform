from config.configuration import EVE_API
from enums.enums import TipTypeEnum
import requests
import json
import traceback
from datetime import datetime
from datetime import date
from utils.logger import get_module_logger

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
        return json.loads(json_obj['response'])
    def update_tip(self, tip_id):
        headers = {
            'Content-Type': 'application/json'
        }
        json_data = {
            'send': True
        }

        req = requests.put(url='{}/tip/{}'.format(
            EVE_API['url'], tip_id), headers=headers, data=json.dumps(json_data))

        json_obj = req.json()

        if json_obj['status'] == 400:
            print('Could not update tip with {}'.format(tip_id))

    def get_all_users_infos(self):
        r = requests.get(url='{}/notify/users-info'.format(EVE_API['url']))
        json_obj = r.json()

        if json_obj['status'] == 400:
            return None

        join_response = json.loads(json_obj['response'])
        return join_response

    def notify(self, user_segment, tip, templateId):
        header = {"Content-Type": "application/json; charset=utf-8",
                  "Authorization": "Basic MDhjNzVmMTAtYzVhZC00MWM4LWJmMWMtMDg0ZDk4NWY4NDQ2"}

        payload = {"app_id": "62f0fa9f-3e8e-4514-92bb-a718d2600362",
                   "included_segments": [user_segment],
                   "template_id":templateId,
                   "contents": {"en": tip}}

        req = requests.post("https://onesignal.com/api/v1/notifications", headers=header, data=json.dumps(payload))
        #Importante
        return req.status_code
        
    def reset(self, tip_type):
        headers = {
            'Content-Type': 'application/json'
        }
        json_data = {
            'tip_type': tip_type
        }

        req = requests.put(url='{}/tip/reset'.format(
            EVE_API['url']), headers=headers, data=json.dumps(json_data))

        json_obj = req.json()

        if json_obj['status'] == 400:
            get_module_logger().info('Could not reset tip with type {}'.format(tip_type))

    def run(self):
        get_module_logger().info("Notification Job is now running...")
        #buscando as dicas de cada tipo de usuário
        pregnant_tip = self.get_tip_by_type(TipTypeEnum.pregnant)
        trying_tip = self.get_tip_by_type(TipTypeEnum.wanting_conceive)
        after_birth_tip = self.get_tip_by_type(TipTypeEnum.after_birth)      

        if(not pregnant_tip):
            get_module_logger().info('Não há dicas de grávidas para enviar, portanto, devemos dar reset.')
            #se ele não encontrou nenhuma dica, podemos ter duas possibilidades: ou ela não existe
            #ou temos que dar reset.
            self.reset(TipTypeEnum.pregnant)
            pregnant_tip = self.get_tip_by_type(TipTypeEnum.pregnant)


        if(not trying_tip):
            get_module_logger().info('Não há dicas tentantes para enviar, portanto, devemos dar reset.')
            self.reset(TipTypeEnum.wanting_conceive)
            trying_tip = self.get_tip_by_type(TipTypeEnum.wanting_conceive)
            # reset

        if(not after_birth_tip):
            get_module_logger().info('Não há dicas de puerperas para enviar, portanto, devemos dar reset.')
            # TODO IMPLEMENTAR AFTER_BIRTH  
        
        if trying_tip:
            trying_template_id = 'c2eace00-74dc-47b3-a5a1-96fbd778c5ca'
            status_code = self.notify("Trying Conceive Users", trying_tip['description'], trying_template_id)
            if status_code == 200:
                self.update_tip(trying_tip['_id']['$oid'])
                get_module_logger().info('Notificação recebida pelos usuários tentantes...')
        if pregnant_tip:
            pregnant_template_id = '2a8b7415-6410-424c-b013-7a1594ea1640'
            status_code = self.notify("Pregnant Users",pregnant_tip['description'], pregnant_template_id)
            if status_code == 200:
                self.update_tip(pregnant_tip['_id']['$oid'])     
                get_module_logger().info('Notificação recebida pelas usuárias grávidas...')  