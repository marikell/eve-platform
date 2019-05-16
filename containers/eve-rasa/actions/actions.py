import requests
import json
import nltk
import pandas as pd
from api.route_config import RouteConfig
from typing import Dict, Text, Any, List, Union, Optional
from rasa_core_sdk import Action
from rasa_core_sdk import Tracker
from rasa_core_sdk import ActionExecutionRejection
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_core_sdk.events import SlotSet
from nltk.stem import RSLPStemmer


route_config = RouteConfig('5001','eve_api')

route_config.register_route('action_subscribe','/action-answer')

# class SubscribeAction(Action):
#   def name(self):
#     return "action_subscribe"

#   def run(self, dispatcher, tracker, domain):
#     intent = tracker.latest_message['intent'].get('name')
#     entities = tracker.latest_message.get('entities', [])

#     entities_obj = [e for e in entities]

#     data = {
#       'entities' : entities_obj,
#       'intent' : intent
#     }

#     headers = {
#       'Content-Type': 'application/json',
#     }

#     req = requests.post(url = route_config.get_route('action_subscribe'),headers= headers,data=json.dumps(data))

#     dispatcher.utter_message(req.json())
#     return

class GetAnswer(Action):
    def name(self):
        return "get_answer"
    def run(self, dispatcher, tracker, domain):
        response = ""
        entities = tracker.latest_message['entities']
        intent = tracker.latest_message['intent'].get('name')
        for entity in entities:
            # stemmer = RSLPStemmer()
            # stem_entity = stemmer.stem(entity['value'])
            data = pd.read_csv('./api/dados.csv', encoding = 'utf-8')
            list_data = data.values.tolist()
            for l in list_data:
                if intent in l and entity['value'] in l:
                    response += str(l[2])
        dispatcher.utter_message(response)

class CancelReminder(Action):
    def name(self):
        return "cancel_reminder"
    def run(self, dispatcher, tracker, domain):
        response = "Ok, lembrete cancelado!"
        dispatcher.utter_message(response)

class MedicineForm(FormAction):
    hours = []
    def name(self):
        return "medicine_form"
        
    @staticmethod
    def required_slots(tracker):
        return [
            "med_name",
            "med_frequency",
            "med_frequency_day",
            "med_hours"
        ]

    def slot_mappings(self):
        return { 
            "med_name": [
                self.from_entity(entity="med_name"),
                self.from_text(intent="enter_data")
            ],
            "med_frequency": [
                self.from_entity(entity="med_frequency"),
                self.from_text(intent="enter_data")
            ],
            "med_frequency_day": [
                self.from_entity(entity="med_frequency_day"),
                self.from_text(intent="enter_data")
            ],
            "med_hours": [
                self.from_entity(entity="med_hours"),
                self.from_text(intent="enter_data")
            ]
        }

    def validate_med_frequency(self,
                         value: Text,
                         dispatcher: CollectingDispatcher,
                         tracker: Tracker,
                         domain: Dict[Text, Any]) -> Optional[Text]:
        if int(value) in [1,2]:
            return {'med_frequency': value}
        else:
            dispatcher.utter_template('utter_wrong_med_frequency', tracker)
            return None

    def validate_med_frequency_day(self,
                         value: Text,
                         dispatcher: CollectingDispatcher,
                         tracker: Tracker,
                         domain: Dict[Text, Any]) -> Optional[Text]:

        if self.is_int(value) and int(value) > 0:
            dispatcher.utter_template('utter_inform_med_hours', tracker)
            return {'med_frequency_day': value}
        else:
            dispatcher.utter_template('utter_wrong_med_frequency_day', tracker)
            return None

    def validate_med_hours(self,
                         value: Text,
                         dispatcher: CollectingDispatcher,
                         tracker: Tracker,
                         domain: Dict[Text, Any]) -> Optional[Text]:
        frequency_day = tracker.get_slot("med_frequency_day")
        if self.is_int(value) and int(value) >= 0 and int(value) <= 23:
            if(len(self.hours) < int(frequency_day)):
                self.hours.append(value)
                if(len(self.hours) == int(frequency_day)):
                    return {'med_hours': self.hours}
            else:
                return {'med_hours': self.hours}
        else:
            dispatcher.utter_template('utter_wrong_med_hours', tracker)
            return None

    @staticmethod
    def is_int(string: Text) -> bool:
        try:
            int(string)
            return True
        except ValueError:
            return False

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any])-> List[Dict]:
        frequency_day = tracker.get_slot("med_frequency_day")
        frequency = tracker.get_slot("med_frequency")
        name = tracker.get_slot("med_name")
        hours = tracker.get_slot("med_hours")
        hours = ", ".join(str(x) for x in hours)
        hours += " horas"

        response = """Vou agendar um lembrete para:\n 
                    - Remédio: {0}\n 
                    - Horário: {1}\n
                    - Frequência: {2}\n 
                    Ok?""".format(name, hours, frequency)
        dispatcher.utter_message(response)
        # dispatcher.utter_template('utter_values_med', tracker)
        return []
    
class ActionGreetUser(Action):
    def name(self):
        return "action_greet_user"

    def run(self, dispatcher, tracker, domain):
        intent = tracker.latest_message["intent"].get("name")
        if intent == "hello":
            dispatcher.utter_template("utter_introduce", tracker)
            dispatcher.utter_template("utter_greet", tracker)
        elif intent == "get_started":
            dispatcher.utter_template("utter_introduce", tracker)
            dispatcher.utter_template("utter_greet", tracker)            
        elif intent == "greeting":
            dispatcher.utter_template("utter_introduce", tracker)
            dispatcher.utter_template("utter_greet_back", tracker)
        return []

class ActionCityUser(Action):
    def name(self):
        return "action_city_user"

    def run(self, dispatcher, tracker, domain):        
        dispatcher.utter_template("utter_great", tracker)
        return []

class ActionStateUser(Action):
    def name(self):
        return "action_state_user"

    def run(self, dispatcher, tracker, domain):        
        dispatcher.utter_template("utter_great", tracker)
        return []

class ActionAgeUser(Action):
    def name(self):
        return "action_age_user"

    def run(self, dispatcher, tracker, domain):        
        dispatcher.utter_template("utter_great", tracker)
        return []