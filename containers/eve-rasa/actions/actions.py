from typing import Any, Text, Dict, List, Optional
from rasa_sdk import Action, Tracker, ActionExecutionRejection
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_sdk.events import SlotSet
from route_config import RouteConfig
import requests
import json

route_config = RouteConfig('http://eve_api:5001')

route_config.register_route('get_answer','/action-answer')

class GetAnswer(Action):
    def name(self) -> Text:
        return "get_answer"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        intent = tracker.latest_message['intent'].get('name')
        entities = tracker.latest_message['entities']
        entities_obj = [e.get('value') for e in entities]

        response = 'Desculpe, nao consegui compreender!'

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

            if json_obj.get('response') is not None:
                response = json_obj['response']
            
            dispatcher.utter_message(response)

        except:
            dispatcher.utter_message(response)

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("Hello World!")

        return []

class ActionGreetUser(Action):
    def name(self) -> Text:
        return "action_greet_user"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

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

class CancelReminder(Action):
    def name(self) -> Text:
        return "cancel_reminder"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = "Ok, lembrete cancelado!"
        dispatcher.utter_message(response)

class MedicineForm(FormAction):
    hours = []
    def name(self) -> Text:
        return "medicine_form"
        
    @staticmethod
    def required_slots(tracker: Tracker):
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

class ActionCityUser(Action):
    def name(self) -> Text:
        return "action_city_user"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:     

        dispatcher.utter_template("utter_great", tracker)

        return []

class ActionStateUser(Action):
    def name(self) -> Text:
        return "action_state_user"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_template("utter_great", tracker)

        return []

class ActionAgeUser(Action):
    def name(self) -> Text:
        return "action_age_user"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:   

        dispatcher.utter_template("utter_great", tracker)

        return []
