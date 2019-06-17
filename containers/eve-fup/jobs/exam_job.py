from config.configuration import EVE_API, RASA_API
import requests 
from helpers.logging import get_log
import json
import traceback

class ExamJob():
    def run(self):
          
        get_log('Starting Exams Job...')
        
        pregnant_users_exams = self.get_pregnant_users_exams()
        exams = self.get_all_exams()

        exams_to_execute = []

        for usr in pregnant_users_exams:
            checked_user_exams = []
            for exm in exams:
                checked_exm = self.check_exam(exm, usr)

                if checked_exm is None:
                    continue

                checked_user_exams.append(checked_exm)
            

            if len(checked_user_exams) == 0:
                continue

            #TODO REMOVE THIS PART (ONLY MADE FOR RASA X)

            user = self.get_user_by_email('me')

            obj = {
                #TODO THIS WILL BE CHANGED TO USER ID
                'user_id': user['email'],
                #TODO SEND ALL EXAMS, NOT ONLY ONE
                'exams' : checked_user_exams[0]
            }
                
            exams_to_execute.append(obj)

        for exm_act in exams_to_execute:
                    
            headers = {
                'Content-Type' : 'application/json'
            }

            try:
                #url do set slot
                url_slot = '{}/conversations/{}/tracker/events'.format(RASA_API['url'], exm_act['user_id'])

                json_data = {
                    
                    'event' : 'slot',
                    'value' : obj['exams']['name'],
                    'name' : 'exam_name'
                }
            
                req = requests.post(url = url_slot,headers= headers,data=json.dumps(json_data))

                json_data = {                    
                    'event' : 'slot',
                    'value' : obj['exams']['_id']['$oid'],
                    'name' : 'exam_id'
                }
            
                req = requests.post(url = url_slot,headers= headers,data=json.dumps(json_data))

                url_action = '{}/conversations/{}/execute'.format(RASA_API['url'],exm_act['user_id'])

                action_data = {
                        
                    "name":"utter_ask_exam"
                }
                
                req_action_data = requests.post(url = url_action, headers = headers, data=json.dumps(action_data))

                action_listen = {
                    "name" : "action_listen"
                }

                req_action_listen = requests.post(url = url_action, headers = headers, data=json.dumps(action_listen))

                get_log('Executed action for {} exam and user {}'.format(obj['exams']['name'], exm_act['user_id']))

                #TODO REMOVE THIS LINE (MADE FOR RASA X ONLY)
                break

            except:
                continue


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

    def get_user_by_email(self, email):
        
        email_obj = {
            
            'email' : email
        }
                
        headers = {
            'Content-Type' : 'application/json'
        }
                
        req_email = requests.post(url = '{}/user/get-by-email'.format(EVE_API['url']),headers = headers, data=json.dumps(email_obj))

        if req_email.json()['status'] == 400:
            get_log(req_email.json()['response'])
            return None
        
        user = json.loads(req_email.json()['response'])

        return user


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

