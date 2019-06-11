from config.configuration import EVE_API
import requests 
from helpers.logging import get_log
import json
import traceback

class ExamJob():
    def run(self):
          
        get_log('Starting Exams Job...')
        
        pregnant_users_exams = self.get_pregnant_users_exams()
        exams = self.get_all_exams()

        objects = []


        for usr in pregnant_users_exams:
            teste = []
            for exm in exams:
                checked_exm = self.check_exam(exm, usr)

                if checked_exm is None:
                    continue

                teste.append(checked_exm)
            

            obj = {
                'user_id': 'me',
                'exams' : teste[0]
            }
                
            objects.append(obj)

            headers = {
            'Content-Type':'application/json'
            }

            url = 'http://localhost:5005/conversations/{}/tracker/events'.format(obj['user_id'])

            json_data = {
                "event" : "slot",
                "value" : obj['exams']['name'],
                "name" : "exam_name" 
            }

            req = requests.post(url = url,headers= headers,data=json.dumps(json_data))

            print(req.json())

            url2 = 'http://localhost:5005/conversations/{}/execute'.format(obj['user_id'])

            action_data = {
                "name":"utter_ask_exam"
            }
            
            req2 = requests.post(url = url2, headers = headers, data=json.dumps(action_data))

            print(req2.json())

            teste = {
                "name" : "action_listen"
            }

            req2 = requests.post(url = url2, headers = headers, data=json.dumps(teste))


    def check_exam(self, exm, usr):

        user_made_exams_ids = [exmusr['exam_id']['$oid'] for exmusr in usr['user_exams']]

        id = exm['_id']['$oid']

        if id in user_made_exams_ids:
            return None
        
        #exames iniciais
        if exm['weeks_start'] == 0:
            return exm
        
        if usr['weeks'] >= exm['weeks_start']:
            if exm['weeks_end'] is None:
                return exm
            return exm if usr['weeks'] <= exm['weeks_end'] else None        
        
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

