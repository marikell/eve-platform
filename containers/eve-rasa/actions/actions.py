from typing import Any, Text, Dict, List, Optional
from rasa_sdk import Action, Tracker, ActionExecutionRejection
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_sdk.events import SlotSet
from rasa_core_sdk.events import UserUtteranceReverted
from route_config import RouteConfig
import requests
import json
import dateutil.parser

route_config = RouteConfig('http://localhost:5001')
route_config.register_route('get_answer','/action-answer')
route_config.register_route('send_slots','/rasa/send-slots')
route_config.register_route('get_exam_by_name','/exam/get-by-name')
route_config.register_route('get_user_by_email','/user/get-by-email')
route_config.register_route('send_slot_user_exam','/rasa/send-slot-user-exam')
route_config.register_route('send_health_slots','/rasa/send-health-slots')
route_config.register_route('send_pregnancy_slots','/rasa/send-pregnancy-slots')
route_config.register_route('send_personal_slots','/rasa/send-personal-slots')
route_config.register_route('user_form','/user-form')
route_config.register_route('get_user_form','/user-form/get-form-user')
route_config.register_route('get_form_by_name','/form/get-by-name')
route_config.register_route('send_unanswered_question','/unanswered-question')

class GetAnswer(Action):
    def name(self) -> Text:
        return "action_get_answer"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        intent = tracker.latest_message['intent'].get('name')
        if(intent == 'last_intent'):
            intent = tracker.get_slot('last_intent')
        entities = tracker.latest_message['entities']
        entities_obj = [e.get('value') for e in entities]
        response = 'Não vou te conseguir ajudar nessa, mas pergunte ao seu médico, ele saberá te responder ;)'
        data = {
            'entities' : entities_obj,
            'intent' : intent
        }
        headers = {
            'Content-Type':'application/json'
        }
        try:        
            req = requests.post(url = route_config.get_route('get_answer'),headers= headers,data=json.dumps(data))
            json_obj = req.json()
            if json_obj.get('response'):
                response = json_obj['response']
            else:
                data = {
                    'question' : tracker.latest_message['text']
                }
                req = requests.post(url = route_config.get_route('send_unanswered_question'),headers= headers,data=json.dumps(data))
            dispatcher.utter_message(response)
        except:
            dispatcher.utter_message(response)
        return [SlotSet("last_intent", intent)]

class ActionGreetUser(Action):
    def name(self) -> Text:
        return "action_greet_user"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_id = tracker.get_slot("user_id")
        headers = { 'Content-Type':'application/json' }
        # busca o id form-initial
        data = { "name" : "form_initial" }
        req = requests.post(route_config.get_route('get_form_by_name'),headers= headers,data=json.dumps(data))
        initial_form_id = req.json()['response']['_id']['$oid']
        
        # verifica se já um registro para esse usuário desse form
        data = {
            'form_id': initial_form_id,
            'user_id': user_id
        }
        req = requests.post(url = route_config.get_route('get_user_form'), headers=headers, data=json.dumps(data))        
        intent = tracker.latest_message["intent"].get("name")
        dispatcher.utter_template("utter_hello", tracker)
        
        if 'response' in req.json() and json.loads(req.json()['response'])['status'] == 1:
            if intent == "hello":
                dispatcher.utter_template("utter_greet", tracker)
            elif intent == "greeting":
                dispatcher.utter_template("utter_greet_back", tracker)
        else:
            if intent == "hello" or intent == "get_started":
                dispatcher.utter_template("utter_introduce", tracker)
                dispatcher.utter_template("utter_ask_info", tracker)
            elif intent == "greeting":
                dispatcher.utter_template("utter_introduce", tracker)
                dispatcher.utter_template("utter_greet_back", tracker)
        
        
        return []

class InitialForm(FormAction):
    def name(self) -> Text:
        return "form_initial"
        
    @staticmethod
    def required_slots(tracker: Tracker):
        user_id = tracker.get_slot("user_id")
        headers = { 'Content-Type':'application/json' }
        # busca o id form-initial
        data = { "name" : "form_initial" }        
        req = requests.post(route_config.get_route('get_form_by_name'),headers= headers,data=json.dumps(data))
        initial_form_id = req.json()['response']['_id']['$oid']
        
        # verifica se já um registro para esse usuário desse form
        data = {
            'form_id': initial_form_id,
            'user_id': user_id
        }
        req = requests.post(url = route_config.get_route('get_user_form'), headers=headers, data=json.dumps(data))
        
        # se o registro não existe, insere
        if 'response' not in req.json():
            data = {
                "user_id" : user_id,
                "form_id" : initial_form_id,
                "status" : 0
            }

            req = requests.post(route_config.get_route('user_form'),headers= headers,data=json.dumps(data))
            user_form_id = json.loads(req.json()['response'])['inserted_id']            

        if(tracker.get_slot('pre_natal') == "False"):
            return []
        elif(tracker.get_slot('first_ultrasound') == "False"):
            return []
        elif(tracker.get_slot('is_pregnant') == "True"):
            return [
                "last_menstruation",
                "first_pregnancy",
                "planned_pregnancy",
                "health_plan",
                "pre_natal",
                "first_ultrasound",
                "first_ultrasound_date"
            ]        
        elif(tracker.get_slot('is_trying') == "True"):
            return [
                "is_planning",
                "has_children",
                "health_plan"
            ]
        elif(tracker.get_slot('is_postpartum') == "True"):
            if(tracker.get_slot('having_sex') == "False"):
                return [
                    "doctor_appointment",
                    "infection",
                    "infection_kind"
                ]
            if(tracker.get_slot('infection') == "False"):
                return []
            
            return [
                "health_plan",
                "planned_pregnancy",
                "breastfeeding",
                "having_sex",
                "contraceptive_method",
                "doctor_appointment",
                "infection",
                "infection_kind"
            ]
        elif(tracker.get_slot('is_pregnant') == "False" and tracker.get_slot('is_trying') == "False" and tracker.get_slot('is_postpartum') == "False"):
            return []
        else:
            return [
                "is_pregnant",
                "is_trying",
                "is_postpartum",
                "last_menstruation",
                "planned_pregnancy",
                "first_pregnancy",
                "health_plan",
                "pre_natal",
                "is_planning",
                "has_children",
                "first_ultrasound",
                "first_ultrasound_date",
                "breastfeeding",
                "having_sex",
                "contraceptive_method",
                "doctor_appointment",
                "infection",
                "infection_kind"
            ]

    def slot_mappings(self):
        return {
            "last_menstruation": [
                self.from_entity(entity="time")
            ],
            "first_ultrasound_date": [
                self.from_entity(entity="time")
            ],
            "contraceptive_method": [
                self.from_entity(entity="contraceptive_method"),
                self.from_text(intent="enter_data")
            ],
            "infection_kind": [
                self.from_entity(entity="infection_kind"),
                self.from_text(intent="enter_data")
            ]
        }

    @staticmethod
    def is_int(string: Text) -> bool:
        try:
            int(string)
            return True
        except ValueError:
            return False

    @staticmethod
    def convert_to_bool(string: str) -> bool:
        return string == 'True'

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any])-> List[Dict]:
        user_id = tracker.get_slot("user_id")
        headers = { 'Content-Type':'application/json' }
        # busca o id form-initial
        data = { "name" : "form_initial" }
        req = requests.post(route_config.get_route('get_form_by_name'),headers= headers,data=json.dumps(data))
        initial_form_id = req.json()['response']['_id']['$oid']
        
        # verifica se já um registro para esse usuário desse form
        data = {
            'form_id': initial_form_id,
            'user_id': user_id
        }
        req = requests.post(url = route_config.get_route('get_user_form'), headers=headers, data=json.dumps(data))        
        obj = json.loads(req.json()['response'])
        data = { 'id': obj['_id']['$oid'], 'status': 1 }        
        req = requests.put(url = '{}/{}'.format(route_config.get_route('user_form'), format(data['id'])),headers= headers,data=json.dumps(data))

        first_pregnancy = self.convert_to_bool(tracker.get_slot("first_pregnancy"))
        has_children = self.convert_to_bool(tracker.get_slot("has_children"))
        health_plan = self.convert_to_bool(tracker.get_slot("health_plan"))
        is_planning = self.convert_to_bool(tracker.get_slot("is_planning"))
        is_pregnant = self.convert_to_bool(tracker.get_slot("is_pregnant"))
        pre_natal = self.convert_to_bool(tracker.get_slot("pre_natal"))
        planned_pregnancy = self.convert_to_bool(tracker.get_slot("planned_pregnancy"))
        is_trying = self.convert_to_bool(tracker.get_slot("is_trying"))
        is_postpartum = self.convert_to_bool(tracker.get_slot("is_postpartum"))
        last_menstruation = tracker.get_slot("last_menstruation")
        first_ultrasound_date = tracker.get_slot("first_ultrasound_date")
        breastfeeding = self.convert_to_bool(tracker.get_slot("breastfeeding"))
        having_sex = self.convert_to_bool(tracker.get_slot("having_sex"))
        contraceptive_method = tracker.get_slot("contraceptive_method")        
        doctor_appointment = self.convert_to_bool(tracker.get_slot("doctor_appointment"))        
        infection = self.convert_to_bool(tracker.get_slot("infection"))
        infection_kind = tracker.get_slot("infection_kind")
        user_id = tracker.get_slot("user_id")

        data = {
            "is_first_pregnancy" : first_pregnancy,
            "has_children" : has_children,
            "has_health_plan" : health_plan,
            "is_planning" : is_planning,
            "is_pregnant" : is_pregnant,
            "is_doing_pre_natal" : pre_natal,
            "is_planned_pregnancy" : planned_pregnancy,
            "is_trying" : is_trying,
            "is_postpartum" : is_postpartum,
            "last_menstruation_date" : last_menstruation,
            "first_ultrasound_date" : first_ultrasound_date,
            "is_breastfeeding" : breastfeeding,
            "is_having_sex" : having_sex,
            "contraceptive_method" : contraceptive_method,
            "had_doctor_appointment" : doctor_appointment,
            "had_infection" : infection,
            "infection_kind" : infection_kind,
        }
        
        headers = {
            'Content-Type':'application/json'
        }
        try:    
            headers = {
                'Content-Type' : 'application/json'
            }
                    
            req = requests.post(url = '{}{}'.format(route_config.get_route('send_slots'),'/{}'.format(user_id)),headers= headers,data=json.dumps(data))
        except Exception as e:
            #this will log in the future
            print(str(e))
        
        dispatcher.utter_template('utter_thank_you', tracker)
        if(is_pregnant):
            if(pre_natal):
                dispatcher.utter_template('utter_doing_right_prenatal', tracker)
            elif(pre_natal == False and health_plan == False):
                dispatcher.utter_template('utter_first_step', tracker)
                dispatcher.utter_template('utter_pre_natal_sus', tracker)
            else:
                dispatcher.utter_template('utter_first_step', tracker)
        elif(is_trying):
            if(is_planning):
                dispatcher.utter_template('utter_doing_right', tracker)
            else:
                dispatcher.utter_template('utter_planning_pregnancy', tracker)
                if(health_plan == False):
                    dispatcher.utter_template('utter_pre_natal_sus', tracker)
                else:
                    dispatcher.utter_template('utter_schedule_gynecologist', tracker)

        return []

class ActionIsBot(Action):
    def name(self):
        return "action_is_bot"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_ask_isbot", tracker)
        return [UserUtteranceReverted()]

class ActionHowOld(Action):
    def name(self):
        return "action_how_old"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_ask_howold", tracker)
        return [UserUtteranceReverted()]

class ActionCongrats(Action):
    def name(self):
        return "action_congrats"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_congrats", tracker)
        return [SlotSet("is_pregnant", "True")]

class ActionWhereFrom(Action):
    def name(self):
        return "action_where_from"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_ask_wherefrom", tracker)
        return [UserUtteranceReverted()]

class ActionWhoIsIt(Action):
    def name(self):
        return "action_who_is_it"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_introduce", tracker)
        return [UserUtteranceReverted()]

class ActionWhatsPossible(Action):
    def name(self):
        return "action_whats_possible"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_explain_whatspossible", tracker)
        return [UserUtteranceReverted()]

class ActionBye(Action):
    def name(self):
        return "action_bye"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_bye", tracker)
        return [UserUtteranceReverted()]

class ActionThankYou(Action):
    def name(self):
        return "action_thank_you"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_welcome", tracker)
        return [UserUtteranceReverted()]

class ActionCantHelp(Action):
    def name(self):
        return "action_cant_help"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_canthelp", tracker)
        return [UserUtteranceReverted()]

class ActionGetExam(Action):
    def name(self) -> Text:
        return "action_get_exam"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        exam_name = tracker.get_slot('exam_name')
        user_exam_id = tracker.get_slot('user_exam_id')

        response = 'Esse é um dos exames básicos do pré-natal!'

        headers = { 'Content-Type':'application/json' }

        try:
            data = {
                "exam_status" : 3,
                'id' : user_exam_id
            }
            req = requests.post(route_config.get_route('send_slot_user_exam'),headers= headers,data=json.dumps(data))
            
            data = { 'exam_name' : exam_name }
            req = requests.post(url = route_config.get_route('get_exam_by_name'),headers= headers,data=json.dumps(data))
            exam = req.json()['response']
            response = str(exam['description'])
            if(exam['trimester'] == 0):
                response = response + "\nEsse exame deve ser feito logo no inicio do pré-natal!"
            else:
                response = response + "\nDeve ser feito no {}º trimestre!".format(exam['trimester'])
            dispatcher.utter_message(response)
        except:
            dispatcher.utter_message(response)        
        finally:
            return []

class ActionSaveExam(Action):
    def name(self):
        return "action_doing_right_exam"

    def run(self, dispatcher, tracker, domain):
        user_exam_id = tracker.get_slot('user_exam_id')
        if(user_exam_id):
            try:
                headers = { 'Content-Type':'application/json' }
                                
                data = {
                    "exam_status" : 2,
                    'id' : user_exam_id
                }
                req = requests.post(route_config.get_route('send_slot_user_exam'),headers= headers,data=json.dumps(data))
            except Exception as e:
                #this will log in the future
                print(str(e))
        dispatcher.utter_template("utter_doing_right_exam", tracker)
        return [UserUtteranceReverted()]

class HealthForm(FormAction):
    def name(self) -> Text:
        return "form_health"
        
    @staticmethod
    def required_slots(tracker: Tracker):
        user_id = tracker.get_slot("user_id")
        headers = { 'Content-Type':'application/json' }
        # busca o id form-initial
        data = { "name" : "form_health" }        
        req = requests.post(route_config.get_route('get_form_by_name'),headers= headers,data=json.dumps(data))
        health_form_id = req.json()['response']['_id']['$oid']
        
        # verifica se já um registro para esse usuário desse form
        data = {
            'form_id': health_form_id,
            'user_id': user_id
        }
        req = requests.post(url = route_config.get_route('get_user_form'), headers=headers, data=json.dumps(data))
        
        # se o registro não existe, insere
        if 'response' not in req.json():
            data = {
                "user_id" : user_id,
                "form_id" : health_form_id,
                "status" : 0
            }

            req = requests.post(route_config.get_route('user_form'),headers= headers,data=json.dumps(data))

        if(tracker.get_slot('regular_medicine') == "False"):
            return [
                "hypothyroidism",
                "hyperthyroidism",
                "diabetes",
                "drug_use",
                "autoimmune_disease",
                "asthma",
                "seropositive",
                "high_pressure"
            ]
        else:
            return [
                "regular_medicine",
                "regular_medicine_name",
                "hypothyroidism",
                "hyperthyroidism",
                "diabetes",
                "drug_use",
                "autoimmune_disease",
                "asthma",
                "seropositive",
                "high_pressure"
            ]

    def slot_mappings(self):
            return {
                "regular_medicine_name": [
                    self.from_entity(entity="med_name"),
                    self.from_text(intent="enter_data")
                ],                
            }
    @staticmethod
    def convert_to_bool(string: str) -> bool:
        return string == 'True'

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any])-> List[Dict]:
        user_id = tracker.get_slot("user_id")
        headers = { 'Content-Type':'application/json' }
        # busca o id form-initial
        data = { "name" : "form_health" }
        req = requests.post(route_config.get_route('get_form_by_name'),headers= headers,data=json.dumps(data))
        health_form_id = req.json()['response']['_id']['$oid']
        
        # verifica se já um registro para esse usuário desse form
        data = {
            'form_id': health_form_id,
            'user_id': user_id
        }
        req = requests.post(url = route_config.get_route('get_user_form'), headers=headers, data=json.dumps(data))        
        obj = json.loads(req.json()['response'])
        data = { 'id': obj['_id']['$oid'], 'status': 1 }        
        req = requests.put(url = '{}/{}'.format(route_config.get_route('user_form'), format(data['id'])),headers= headers,data=json.dumps(data))

        regular_medicine = self.convert_to_bool(tracker.get_slot("regular_medicine"))
        regular_medicine_name = tracker.get_slot("regular_medicine_name")
        hypothyroidism = self.convert_to_bool(tracker.get_slot("hypothyroidism"))
        hyperthyroidism = self.convert_to_bool(tracker.get_slot("hyperthyroidism"))
        diabetes = self.convert_to_bool(tracker.get_slot("diabetes"))
        drug_use = self.convert_to_bool(tracker.get_slot("drug_use"))
        autoimmune_disease = self.convert_to_bool(tracker.get_slot("autoimmune_disease"))
        asthma = self.convert_to_bool(tracker.get_slot("asthma"))
        seropositive = self.convert_to_bool(tracker.get_slot("seropositive"))
        high_pressure = self.convert_to_bool(tracker.get_slot("high_pressure"))

        data = {
            "takes_regular_medicine" : regular_medicine,
            "regular_medicine_name" : regular_medicine_name,
            "has_hypothyroidism" : hypothyroidism,
            "has_hyperthyroidism" : hyperthyroidism,
            "has_diabetes" : diabetes,
            "drug_use" : drug_use,
            "has_autoimmune_disease" : autoimmune_disease,
            "has_asthma" : asthma,
            "is_seropositive" : seropositive,
            "has_high_pressure" : high_pressure
        }
        
        headers = {
            'Content-Type':'application/json'
        }
        try:        
            email_obj = {                
                'email' : 'me'
            }
                    
            headers = {
                'Content-Type' : 'application/json'
            }
                    
            req_email = requests.post(url = '{}'.format(route_config.get_route('get_user_by_email')),headers = headers, data=json.dumps(email_obj))

            if req_email.json()['status'] == 200:
                user_id = json.loads(req_email.json()['response'])['_id']['$oid']
                req = requests.post(url = '{}{}'.format(route_config.get_route('send_health_slots'),'/{}'.format(user_id)),headers= headers,data=json.dumps(data))
        except Exception as e:
            #this will log in the future
            print(str(e))
                
        dispatcher.utter_template('utter_thank_you', tracker)
        dispatcher.utter_template('utter_ask_me_anything', tracker)
        return []

class PersonalForm(FormAction):
    def name(self) -> Text:
        return "form_personal"
        
    @staticmethod
    def required_slots(tracker: Tracker):
        user_id = tracker.get_slot("user_id")
        headers = { 'Content-Type':'application/json' }
        # busca o id form-initial
        data = { "name" : "form_personal" }        
        req = requests.post(route_config.get_route('get_form_by_name'),headers= headers,data=json.dumps(data))
        personal_form_id = req.json()['response']['_id']['$oid']
        print(personal_form_id)
        # verifica se já um registro para esse usuário desse form
        data = {
            'form_id': personal_form_id,
            'user_id': user_id
        }
        req = requests.post(url = route_config.get_route('get_user_form'), headers=headers, data=json.dumps(data))
        
        # se o registro não existe, insere
        if 'response' not in req.json():
            data = {
                "user_id" : user_id,
                "form_id" : personal_form_id,
                "status" : 0
            }
            print(data)

            req = requests.post(route_config.get_route('user_form'),headers= headers,data=json.dumps(data))
        return [
            "height",
            "weight",
            "state"
        ]

    def slot_mappings(self):
            return {
                "height": [
                    self.from_entity(entity="number")
                ],
                "weight": [
                    self.from_entity(entity="number")
                ],
                "state": [
                    self.from_text(intent="enter_data"),
                    self.from_entity(entity="state")
                ],
            }

    def validate_height(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        print(value)
        if(self.is_int(value) and int(value) > 150):
            return {"height": value}
        else:
            dispatcher.utter_template("utter_wrong_height", tracker)
            return {"height": None}

    def validate_weight(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        if(self.is_int(value) and int(value) > 40):
            return {"weight": value}
        else:
            dispatcher.utter_template("utter_wrong_weight", tracker)
            return {"weight": None}
    
    def validate_state(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        if value.upper() in self.state_db():
            return {"state": value}
        else:
            dispatcher.utter_template("utter_wrong_state", tracker)
            return {"state": None}

    @staticmethod
    def state_db() -> List[Text]:
        return [
            "SP",
            "AM",
            "RS",
            "RJ",
            "MG",
            "AP",
            "AC",
            "AL",
            "BA",
            "CE",
            "ES",
            "GO",
            "MA",
            "MT",
            "MS",
            "PA",
            "PB",
            "PR",
            "PE",
            "PI",
            "RN",
            "RO",
            "RR",
            "SC",
            "SE",
            "TO",
            "DF"
        ]

    @staticmethod
    def convert_to_bool(string: str) -> bool:
        return string == 'True'

    @staticmethod
    def is_int(string: Text) -> bool:
        try:
            int(string)
            return True
        except ValueError:
            return False

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any])-> List[Dict]:
        user_id = tracker.get_slot("user_id")
        headers = { 'Content-Type':'application/json' }
        # busca o id form-initial
        data = { "name" : "form_personal" }
        req = requests.post(route_config.get_route('get_form_by_name'),headers= headers,data=json.dumps(data))
        personal_form_id = req.json()['response']['_id']['$oid']
        
        # verifica se já um registro para esse usuário desse form
        data = {
            'form_id': personal_form_id,
            'user_id': user_id
        }
        req = requests.post(url = route_config.get_route('get_user_form'), headers=headers, data=json.dumps(data))        
        obj = json.loads(req.json()['response'])
        data = { 'id': obj['_id']['$oid'], 'status': 1 }        
        req = requests.put(url = '{}/{}'.format(route_config.get_route('user_form'), format(data['id'])),headers= headers,data=json.dumps(data))

        height = tracker.get_slot("height")
        weight = tracker.get_slot("weight")
        state = tracker.get_slot("state")

        data = {
            "height" : int(height),
            "weight" : int(weight),
            "state" : state
        }
        
        headers = {
            'Content-Type':'application/json'
        }
        try:        
            email_obj = {                
                'email' : 'me'
            }
            headers = {
                'Content-Type' : 'application/json'
            }
            req_email = requests.post(url = '{}'.format(route_config.get_route('get_user_by_email')),headers = headers, data=json.dumps(email_obj))
            if req_email.json()['status'] == 200:
                user_id = json.loads(req_email.json()['response'])['_id']['$oid']
                req = requests.post(url = '{}{}'.format(route_config.get_route('send_personal_slots'),'/{}'.format(user_id)),headers= headers,data=json.dumps(data))
                print(req)

        except Exception as e:
            #this will log in the future
            print(str(e))
                
        dispatcher.utter_template('utter_thank_you', tracker)
        dispatcher.utter_template('utter_ask_me_anything', tracker)
        return []

class PregnancyForm(FormAction):
    def name(self) -> Text:
        return "form_pregnancy"
        
    @staticmethod
    def required_slots(tracker: Tracker):
        user_id = tracker.get_slot("user_id")
        headers = { 'Content-Type':'application/json' }
        # busca o id form-initial
        data = { "name" : "form_pregnancy" }        
        req = requests.post(route_config.get_route('get_form_by_name'),headers= headers,data=json.dumps(data))
        pregnancy_form_id = req.json()['response']['_id']['$oid']
        
        # verifica se já um registro para esse usuário desse form
        data = {
            'form_id': pregnancy_form_id,
            'user_id': user_id
        }
        req = requests.post(url = route_config.get_route('get_user_form'), headers=headers, data=json.dumps(data))
        
        # se o registro não existe, insere
        if 'response' not in req.json():
            data = {
                "user_id" : user_id,
                "form_id" : pregnancy_form_id,
                "status" : 0
            }

            req = requests.post(route_config.get_route('user_form'),headers= headers,data=json.dumps(data))
        if(tracker.get_slot('births') is not None):
            if(tracker.get_slot('normal_births') is not None):
                if(int(tracker.get_slot('births')) == int(tracker.get_slot('normal_births'))):
                    return [
                        "abortion",
                        "premature_birth"
                    ]
                elif(int(tracker.get_slot('births')) > int(tracker.get_slot('normal_births'))):
                    return [
                        "why_cesarean_birth",
                        "abortion",
                        "premature_birth"
                    ]
            else:
                return [
                    "normal_births",
                    "why_cesarean_birth",
                    "abortion",
                    "premature_birth"
                ]
        if(tracker.get_slot('had_birth') == "False"):
            return [
                "abortion"
            ]
        if(tracker.get_slot('had_birth') == "True"):
            return [
                "births",
                "normal_births",
                "why_cesarean_birth",
                "abortion",
                "premature_birth"
            ]        
        else:
            return [
                "high_risk",
                "due_date",
                "had_birth",
                "births",
                "normal_births",
                "why_cesarean_birth",
                "abortion",
                "premature_birth"
            ]

    def slot_mappings(self):
            return {
                "due_date": [
                    self.from_entity(entity="time"),
                    self.from_text(intent="enter_data")
                ],
                "births": [
                    self.from_entity(entity="number")
                ],
                "normal_births": [
                    self.from_entity(entity="number")
                ],
                "why_cesarean_birth": [
                    self.from_text(intent="why_cesarean_answer"),
                    self.from_intent(intent="dont_know", value="Não sei"),
                ],
            }

    def validate_due_date(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        try: 
            date = dateutil.parser.parse(value)
            return {"due_date": value}
        except ValueError:
            dispatcher.utter_template("utter_wrong_due_date", tracker)
            return {"due_date": None}

    def validate_births(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        if(self.is_int(value)):             
            return {"births": value}
        else:
            dispatcher.utter_template("utter_wrong_births", tracker)
            return {"births": None}
    
    def validate_normal_births(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        if(self.is_int(value)):             
            return {"normal_births": value}
        else:
            dispatcher.utter_template("utter_wrong_normal_births", tracker)
            return {"normal_births": None}
    
    @staticmethod
    def is_int(string: Text) -> bool:
        try:
            int(string)
            return True
        except ValueError:
            return False

    @staticmethod
    def convert_to_bool(string: str) -> bool:
        return string == 'True'

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any])-> List[Dict]:
        user_id = tracker.get_slot("user_id")
        headers = { 'Content-Type':'application/json' }
        # busca o id form-initial
        data = { "name" : "form_pregnancy" }
        req = requests.post(route_config.get_route('get_form_by_name'),headers= headers,data=json.dumps(data))
        pregnancy_form_id = req.json()['response']['_id']['$oid']
        
        # verifica se já um registro para esse usuário desse form
        data = {
            'form_id': pregnancy_form_id,
            'user_id': user_id
        }
        req = requests.post(url = route_config.get_route('get_user_form'), headers=headers, data=json.dumps(data))        
        obj = json.loads(req.json()['response'])
        data = { 'id': obj['_id']['$oid'], 'status': 1 }        
        req = requests.put(url = '{}/{}'.format(route_config.get_route('user_form'), format(data['id'])),headers= headers,data=json.dumps(data))

        current_high_risk = self.convert_to_bool(tracker.get_slot("high_risk"))
        due_date = tracker.get_slot("due_date")
        births = tracker.get_slot("births")
        had_birth = self.convert_to_bool(tracker.get_slot("had_birth"))
        normal_births = tracker.get_slot("normal_births")
        why_cesarean_birth = tracker.get_slot("why_cesarean_birth")
        abortion = self.convert_to_bool(tracker.get_slot("abortion"))
        premature_birth = self.convert_to_bool(tracker.get_slot("premature_birth"))
        
        data = {
            "current_high_risk" : current_high_risk,
            "due_date" : due_date,
            "births" : births,
            "cesarean_births" : None if not had_birth else (int(births) - int(normal_births)),
            "normal_births" : normal_births,
            "why_cesarean_birth" : why_cesarean_birth,
            "abortion" : abortion,
            "premature_birth" : premature_birth
        }
        
        headers = {
            'Content-Type':'application/json'
        }
        try:        
            email_obj = {                
                'email' : 'me'
            }
                    
            headers = {
                'Content-Type' : 'application/json'
            }
                    
            req_email = requests.post(url = '{}'.format(route_config.get_route('get_user_by_email')),headers = headers, data=json.dumps(email_obj))

            if req_email.json()['status'] == 200:
                user_id = json.loads(req_email.json()['response'])['_id']['$oid']
                req = requests.post(url = '{}{}'.format(route_config.get_route('send_pregnancy_slots'),'/{}'.format(user_id)),headers= headers,data=json.dumps(data))
        except Exception as e:
            #this will log in the future
            print(str(e))
                
        dispatcher.utter_template('utter_thank_you', tracker)
        dispatcher.utter_template('utter_ask_me_anything', tracker)
        return []