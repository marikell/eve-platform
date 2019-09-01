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
        
        intent = tracker.latest_message["intent"].get("name")
        # verificar se o usuário já existe
        if intent == "hello" or intent == "get_started":
            dispatcher.utter_template("utter_hello", tracker)
            dispatcher.utter_template("utter_introduce", tracker)
            dispatcher.utter_template("utter_ask_info", tracker)
        elif intent == "greeting":
            dispatcher.utter_template("utter_hello", tracker)
            dispatcher.utter_template("utter_introduce", tracker)
            dispatcher.utter_template("utter_greet_back", tracker)
        return []

class InitialForm(FormAction):
    def name(self) -> Text:
        return "form_initial"
        
    @staticmethod
    def required_slots(tracker: Tracker):
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
        elif(tracker.get_slot('is_pregnant') == "False" and tracker.get_slot('is_trying') == "False"):
            return []
        else:
            return [
                "is_pregnant",
                "is_trying",
                "last_menstruation",
                "planned_pregnancy",
                "first_pregnancy",
                "health_plan",
                "pre_natal",
                "is_planning",
                "has_children",
                "health_plan",
                "first_ultrasound",
                "first_ultrasound_date"
            ]

    def slot_mappings(self):
        return {
            "last_menstruation": [
                self.from_entity(entity="time")
            ],
            "first_ultrasound_date": [
                self.from_entity(entity="time")
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
        first_pregnancy = self.convert_to_bool(tracker.get_slot("first_pregnancy"))
        has_children = self.convert_to_bool(tracker.get_slot("has_children"))
        health_plan = self.convert_to_bool(tracker.get_slot("health_plan"))
        is_planning = self.convert_to_bool(tracker.get_slot("is_planning"))
        is_pregnant = self.convert_to_bool(tracker.get_slot("is_pregnant"))
        pre_natal = self.convert_to_bool(tracker.get_slot("pre_natal"))
        planned_pregnancy = self.convert_to_bool(tracker.get_slot("planned_pregnancy"))
        is_trying = self.convert_to_bool(tracker.get_slot("is_trying"))
        last_menstruation = tracker.get_slot("last_menstruation")
        first_ultrasound_date = tracker.get_slot("first_ultrasound_date")

        data = {
            "is_first_pregnancy" : first_pregnancy,
            "has_children" : has_children,
            "has_health_plan" : health_plan,
            "is_planning" : is_planning,
            "is_pregnant" : is_pregnant,
            "is_doing_pre_natal" : pre_natal,
            "is_planned_pregnancy" : planned_pregnancy,
            "is_trying" : is_trying,
            "last_menstruation_date" : last_menstruation,
            "first_ultrasound_date" : first_ultrasound_date
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
                req = requests.post(url = '{}{}'.format(route_config.get_route('send_slots'),'/{}'.format(user_id)),headers= headers,data=json.dumps(data))
        except Exception as e:
            #this will log in the future
            print(str(e))
        
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

class MedicineForm(FormAction):
    def name(self) -> Text:
        return "form_medicine"
        
    @staticmethod
    def required_slots(tracker: Tracker):
        if(tracker.get_slot('med_frequency') == "one_time"):
            return [
                "med_name",
                "med_date"
            ]
        elif(tracker.get_slot('med_frequency') == "daily"):
            return [
                "med_name",
                "med_hour"
            ]
        elif(tracker.get_slot('med_frequency') == "weekly"):
            return [
                "med_name",
                "med_week_day",
                "med_hour"
            ]
        else:
            return [
                "med_frequency",
                "med_name",
                "med_week_day",
                "med_hour",
                "med_date"
            ]


    def slot_mappings(self):
        return {
            "med_week_day": [
                self.from_entity(entity="week_day"),
                self.from_text(intent="enter_data")
            ],
            "med_hour": [
                self.from_entity(entity="hour"),
                self.from_text(intent="enter_data")
            ],
            "med_date": [
                self.from_entity(entity="time")
            ]   
        }
    
    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any])-> List[Dict]:
        med_name = tracker.get_slot("med_name")
        med_frequency = tracker.get_slot("med_frequency")
        med_week_day = tracker.get_slot("med_week_day")
        med_hour = tracker.get_slot("med_hour")
        med_date = tracker.get_slot("med_date")
        
        response = "Confirmando então, você tem que tomar {}".format(med_name)
        if(med_frequency == "one_time"):
            date = dateutil.parser.parse(med_date)
            response = response + " no dia {} às {} horas. \nCerto?".format(date.strftime("%d/%m/%y"), date.strftime("%H"))
        elif(med_frequency == "weekly"):
            response = response + " toda {} às {} horas. \nCerto?".format(med_week_day, med_hour)
        elif(med_frequency == "daily"):
            response = response + " todo dia às {} horas. \nCerto?".format(med_hour)
        
        # salvar as informações
        dispatcher.utter_message(response)
        return []

class AppointmentForm(FormAction):
    def name(self) -> Text:
        return "form_appointment"
        
    @staticmethod
    def required_slots(tracker: Tracker):
        return [
            "app_doc_name",
            "app_date"
        ]
        
    def slot_mappings(self):
        return {
            "app_doc_name": [
                self.from_entity(entity="doc_name"),
                self.from_text(intent="enter_data")
            ],
            "app_date": [
                self.from_entity(entity="time")
            ]   
        }
    
    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any])-> List[Dict]:
        app_doc_name = tracker.get_slot("app_doc_name")
        app_date = tracker.get_slot("app_date")
        date = dateutil.parser.parse(app_date)
        response = "Confirmando então, você tem uma consulta no dia {} com o Dr. {}. Certo?".format(date.strftime("%d/%m/%y"), app_doc_name)

        # salvar as informações
        dispatcher.utter_message(response)
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

class ActionCancelReminder(Action):
    def name(self):
        return "action_cancel_reminder"

    def run(self, dispatcher, tracker, domain):
        # cancelar o lembrete
        dispatcher.utter_template("utter_cancel_reminder", tracker)

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
                "exam_status" : 4,
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
                    "exam_status" : 3,
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
        return [
            "height",
            "weight",
            "date_birth",
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
                "date_birth": [
                    self.from_entity(entity="time")
                ],
                "state": [
                    self.from_text(intent="enter_data"),
                    self.from_entity(entity="state")
                ],
            }

    def validate_date_birth(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        try: 
            date = dateutil.parser.parse(value)
            return {"date_birth": value}
        except ValueError:
            dispatcher.utter_template("utter_wrong_date_birth", tracker)
            return {"date_birth": None}

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
        height = tracker.get_slot("height")
        weight = tracker.get_slot("weight")
        date_birth = tracker.get_slot("date_birth")
        state = tracker.get_slot("state")

        data = {
            "height" : int(height),
            "weight" : int(weight),
            "date_birth" : date_birth,
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