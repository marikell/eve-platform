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
    print('[eve-producer] {}'.format(string))

EVE_API:dict = {
    'url' : 'http://eve_api:5001/api'
}

RASA_API:dict = {
    'url' : 'http://eve_core:5005'
}

class SendExamJob():
    def run(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='eve_rabbit', port=5672))
        channel = connection.channel()
        channel.queue_declare(queue='exams')
        
        users_exams = self.get_users_exams()

        for usr in users_exams:
            usr_exm = self.check_exam(usr, usr['exm'])
            if not usr_exm:
                exm = usr['exm']
                obj = {
                    'user_id' : usr['user_id']['$oid'],
                    'exam_id' : exm[0]['_id']['$oid'],
                    'exam_status' : 0
                }
                inserted = json.loads(self.insert_user_exam(obj))                
                if(inserted):
                    msg = {
                        'user_id' : usr['user_id']['$oid'],
                        'exam_id' : exm[0]['_id']['$oid'],
                        'user_exam_id' : inserted['inserted_id'],
                        'exam_name' : exm[0]['name']
                    }
                    channel.basic_publish(exchange='', routing_key='exams', body=json.dumps(msg))
                    get_log('User {} - Exam {}: sent to queue.'.format(usr['user_id']['$oid'], exm[0]['name']))
        
        get_log('Job finalizado!')
        connection.close()
    
    #verifica se o usuário possui registro na tabela user_exam para esse exame
    def check_exam(self, usr, exm):
        url = '{}/user-exam/{}/{}'.format(EVE_API['url'], usr['user_id']['$oid'], exm[0]['_id']['$oid'])        
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
        
    def get_users_exams(self):
        r = requests.get(url = '{}/fup/users-with-exams'.format(EVE_API['url']))
        json_obj = r.json()

        if json_obj['status'] == 400:
            get_log(json_obj['response'])
            return

        join_response = json.loads(json_obj['response'])
        return join_response

    def insert_user_exam(self, usr_exm):
        headers = {
            'Content-Type':'application/json'
        }
        url = '{}/user-exam'.format(EVE_API['url'])

        r = requests.post(url, data=json.dumps(usr_exm), headers=headers)
        
        json_obj = r.json()

        if json_obj['status'] == 201:
            return json_obj['response']
        
        get_log(json_obj['response'])
        return



schedule.every().day.at(os.environ['RUN_TIME']).do(SendExamJob().run)
get_module_logger().info("Exam Sender is going to run at {}...".format(os.environ['RUN_TIME']))
while True:
    log_times = 0
    try:
        schedule.run_pending()
        time.sleep(10)
    except Exception as e:
        log_times = log_times + 1
        if log_times <= 10:
            get_module_logger().info("[ERROR] {}".format(str(e)))