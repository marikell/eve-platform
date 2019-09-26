import schedule
import time
import requests
import json
import os
import schedule
import time
import traceback
from datetime import datetime
from datetime import date
import logging
import requests 
import json
import traceback
import pika


def get_module_logger():
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s [%(name)-12s] %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger

def get_log(string):
    print('[eve-consumer] {}'.format(string))

EVE_API:dict = {
    'url' : 'http://eve_api:5001/api'
}

RASA_API:dict = {
    'url' : 'http://eve_core:5005'
}

# status dos exames: 0 (fila), 1 (pendente), 2 (feito), 3 (não feito)

class ReceiveExamJob():
    def run(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='eve_rabbit', port=5672))
        channel = connection.channel()
        channel.queue_declare(queue='exams')
        
        get_log('Starting Receive Exams Job...')
        
        channel.basic_consume(queue='exams', on_message_callback=self.callback, auto_ack=True)
        get_log(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()

    def callback(self, ch, method, properties, body):
        obj = json.loads(body)
        pendings_exams = self.check_pending_exams(obj['user_id'])
        
        if pendings_exams is None:
            self.send_exam_to_rasa(obj)
            self.update_user_exam_status(obj['user_exam_id'])
        else:
            self.delete_user_exam(obj['user_exam_id'])
        get_log(" [x] Received %r" % body)

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

            # url_action = '{}/conversations/{}/execute'.format(RASA_API['url'],obj['user_id'])
            url_action = '{}/webhooks/rest/webhook'.format(RASA_API['url'])
            # action_data = { "name":"utter_ask_exam" }
            intent_data = { "sender": obj['user_id'], "message": "/ask_exam" }
            
            req_action_data = requests.post(url = url_action, headers = headers, data=json.dumps(intent_data))

            # action_listen = { "name" : "action_listen" }

            # req_action_listen = requests.post(url = url_action, headers = headers, data=json.dumps(action_listen))
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

schedule.every().day.at(os.environ['RUN_TIME']).do(ReceiveExamJob().run)
get_module_logger().info("Exam Consumer is going to run at {}...".format(os.environ['RUN_TIME']))
while True:
    log_times = 0
    try:
        schedule.run_pending()
        time.sleep(10)
    except Exception as e:
        log_times = log_times + 1
        if log_times <= 10:
            get_module_logger().info("[ERROR] {}".format(str(e)))