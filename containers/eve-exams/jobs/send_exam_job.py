from config.configuration import EVE_API, RASA_API
import requests 
from helpers.logging import get_log
import json
import traceback
import pika
#status dos exames: 0 (fila), 1 (pendente), 2 (done), 3 (undone)

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
