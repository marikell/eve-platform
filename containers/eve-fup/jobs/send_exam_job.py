from config.configuration import EVE_API, RASA_API
import requests 
from helpers.logging import get_log
import json
import traceback
import pika
#status dos exames: 0 (fila), 1 (pendente), 2 (done), 3 (undone)

class SendExamJob():
    def run(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672))
        channel = connection.channel()
        channel.queue_declare(queue='exams')
        
        pregnant_users_exams = self.get_pregnant_users_exams()
        exams = self.get_all_exams()

        for usr in pregnant_users_exams:
            for exm in exams:
                checked_exm = self.check_exam(exm, usr)

                if checked_exm is None:
                    continue
                
                obj = {
                    'user_id' : usr['user_id']['$oid'],
                    'exam_id' : exm['_id']['$oid'],
                    'exam_status' : 0
                }
                
                if(self.insert_user_exam(obj)):
                    msg = {
                        'user' : usr['user_id']['$oid'],
                        'exam_name' : checked_exm['name'],
                        'exam_slot' : checked_exm['slot']
                    }

                    channel.basic_publish(exchange='', routing_key='exams', body=json.dumps(msg))
                    print('User {} - Exam {}: sent to queue.'.format(usr['user_id']['$oid'], checked_exm['name']))
        
        connection.close()
        
    def check_exam(self, exm, usr):
        user_made_exams_ids = [exmusr['exam_id']['$oid'] for exmusr in usr['user_exams']]
        id = exm['_id']['$oid']

        if id in user_made_exams_ids:
            return None

        if exm['trimester'] == 0 or (usr['user_trimesters'][0]['trimester'] >= exm['trimester']):
            return exm
        
        return None

    def get_pregnant_users_exams(self):
        r = requests.get(url = '{}/fup/pregnant-users-with-exams'.format(EVE_API['url']))

        json_obj = r.json()

        if json_obj['status'] == 400:
            get_log(json_obj['response'])
            return

        join_response = json.loads(json_obj['response'])
        
        return join_response

    def get_all_exams(self):
        r = requests.get(url = '{}/exam'.format(EVE_API['url']))

        json_obj = r.json()

        if json_obj['status'] == 400:
            get_log(json_obj['response'])
            return

        return json_obj['response']

    def insert_user_exam(self, usr_exm):
        headers = {
            'Content-Type':'application/json'
        }
        url = '{}/user-exam'.format(EVE_API['url'])

        r = requests.post(url, data=json.dumps(usr_exm), headers=headers)
        
        json_obj = r.json()

        if json_obj['status'] == 201:
            return True
        
        get_log(json_obj['response'])
        return


