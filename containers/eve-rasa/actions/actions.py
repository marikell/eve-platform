from typing import Any, Text, Dict, List, Optional
from rasa_sdk import Action, Tracker, ActionExecutionRejection
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_sdk.events import SlotSet
from route_config import RouteConfig
import requests
import json

route_config = RouteConfig('http://localhost:5001')
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

class ActionGreetUser(Action):
    def name(self) -> Text:
        return "action_greet_user"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        intent = tracker.latest_message["intent"].get("name")
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
    hours = []
    def name(self) -> Text:
        return "initial_form"
        
    @staticmethod
    def required_slots(tracker: Tracker):
        return [
            "pregnancy_weeks",
            "planned_pregnancy",
            "first_pregnancy",
            "health_plan",
            "pre_natal"
        ]

    def slot_mappings(self):
        return {
            "pregnancy_weeks": [
                self.from_entity(entity="pregnancy_weeks"),
                self.from_text(intent="enter_data")
            ],
            "planned_pregnancy": [
                self.from_text(intent="enter_data")
            ],
            "first_pregnancy": [
                self.from_text(intent="enter_data")
            ],
            "health_plan": [
                self.from_text(intent="enter_data")
            ],
            "pre_natal": [
                self.from_text(intent="enter_data")
            ]
        }

    def validate_pregnancy_weeks(self,
                            value: Text,
                            dispatcher: CollectingDispatcher,
                            tracker: Tracker,
                            domain: Dict[Text, Any]) -> Optional[Text]:        
        if self.is_int(value) and int(value) >= 1 and int(value) <= 40:            
            return {'pregnancy_weeks': value}
        else:
            dispatcher.utter_template('utter_wrong_pregnancy_weeks', tracker)
            return None

    @staticmethod
    def is_int(string: Text) -> bool:
        try:
            int(string)
            return True
        except ValueError:
            return False

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any])-> List[Dict]:
        planned_pregnancy = tracker.get_slot("planned_pregnancy")
        first_pregnancy = tracker.get_slot("first_pregnancy")
        health_plan = tracker.get_slot("health_plan")
        pre_natal = tracker.get_slot("pre_natal")
        # salva as informações
        dispatcher.utter_template('utter_thank_you', tracker)
        return []