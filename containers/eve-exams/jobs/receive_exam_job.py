from config.configuration import EVE_API, RASA_API
import requests 
from helpers.logging import get_log
import json
import traceback
import pika
# status dos exames: 0 (fila), 1 (pendente), 2 (feito), 3 (não feito)

class ReceiveExamJob():
    def run(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='eve_rabbit', port=5672))
        channel = connection.channel()
        channel.queue_declare(queue='exams')
        
        get_log('Starting Exams Job...')
        
        channel.basic_consume(queue='exams', on_message_callback=self.callback, auto_ack=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()

    def callback(self, ch, method, properties, body):
        obj = json.loads(body)
        pendings_exams = self.check_pending_exams(obj['user_id'])
        pendings_forms = self.check_pending_forms(obj['user_id'])
        if pendings_exams is None and pendings_forms is None:
            self.send_exam_to_rasa(obj)
            self.update_user_exam_status(obj['user_exam_id'])
        else:
            self.delete_user_exam(obj['user_exam_id'])
        print(" [x] Received %r" % body)

    def check_pending_exams(self, usr):
        url = '{}/user-exam/{}'.format(EVE_API['url'], usr)
        r = requests.get(url)
        
        json_obj = r.json()
        
        if json_obj['status'] == 400:
            get_log(json_obj['response'])
            return
        
        try:
            response = json.loads(json_obj['response'])
        except KeyError:
            response = None
        
        return response
    
    def check_pending_forms(self, usr):
        url = '{}/user-form/{}/{}'.format(EVE_API['url'], usr, 0)
        r = requests.get(url)
        json_obj = r.json()
        
        if json_obj['status'] == 400:
            get_log(json_obj['response'])
            return
        try:
            response = json.loads(json_obj['response'])
        except KeyError:
            response = None
        
        return response
    
    def send_exam_to_rasa(self, obj):
        try:
            #TODO REMOVE THIS PART (ONLY MADE FOR RASA 
            obj['user_id'] = obj['user_id']
            
            headers = { 'Content-Type' : 'application/json' }
            url_slot = '{}/conversations/{}/tracker/events'.format(RASA_API['url'], obj['user_id'])

            json_data = {
                'event' : 'slot',
                'value' : obj['exam_name'],
                'name' : 'exam_name'
            }
        
            req = requests.post(url = url_slot,headers= headers,data=json.dumps(json_data))

            json_data = {                    
                'event' : 'slot',
                'value' : obj['exam_id'],
                'name' : 'exam_id'
            }
        
            req = requests.post(url = url_slot,headers= headers,data=json.dumps(json_data))

            json_data = {                    
                'event' : 'slot',
                'value' : obj['user_exam_id'],
                'name' : 'user_exam_id'
            }
        
            req = requests.post(url = url_slot,headers= headers,data=json.dumps(json_data))

            url_action = '{}/conversations/{}/execute'.format(RASA_API['url'],obj['user_id'])

            action_data = { "name":"utter_ask_exam" }
            
            req_action_data = requests.post(url = url_action, headers = headers, data=json.dumps(action_data))

            action_listen = { "name" : "action_listen" }

            req_action_listen = requests.post(url = url_action, headers = headers, data=json.dumps(action_listen))
        except Exception as e:
            print(str(e))
            
    def update_user_exam_status(self, user_exam_id):
        headers = { 'Content-Type' : 'application/json' }
        data = { 'exam_status': 1 }
        url = '{}/user-exam/{}'.format(EVE_API['url'], user_exam_id)
        r = requests.put(url, data=json.dumps(data), headers=headers)
        
        json_obj = r.json()
        
        if json_obj['status'] == 400:
            get_log(json_obj['response'])
            return

    def get_user_by_email(self, email):
        email_obj = { 'email' : email }
                
        headers = { 'Content-Type' : 'application/json' }
                
        req_email = requests.post(url = '{}/user/get-by-email'.format(EVE_API['url']),headers = headers, data=json.dumps(email_obj))

        if req_email.json()['status'] == 400:
            get_log(req_email.json()['response'])
            return None
        
        user = json.loads(req_email.json()['response'])

        return user
    
    def delete_user_exam(self, usr_exm):
        req = requests.delete(url = '{}/user-exam/{}'.format(EVE_API['url'], usr_exm))
        json_obj = req.json()

        if json_obj['status'] == 400:
            get_log(json_obj['response'])
            return
        