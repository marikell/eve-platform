from config.configuration import EVE_API
import requests 
from helpers.logging import get_log
import json
import traceback

#escopo do serviço: para cada usuário do sistema, verificar se já está na hora
#de realizar determinado exame, ou seja, por exame

#query para trazer todas as gravidas que 
class ExamJob():
    def run(self):
          
        get_log('Starting Exams Job...')
        #buscando todos os exames
        
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
                'user_id':usr['user_id'],
                'exams' : teste
            }
                
            objects.append(obj)


        print(objects)

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

