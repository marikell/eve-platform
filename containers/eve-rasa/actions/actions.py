import requests
import json
from api.route_config import RouteConfig
from rasa_core_sdk import Action

route_config = RouteConfig('5001','eve_api')

route_config.register_route('action_subscribe','/action-answer')

class SubscribeAction(Action):
  def name(self):
    return "action_subscribe"

  def run(self, dispatcher, tracker, domain):
    intent = tracker.latest_message['intent'].get('name')
    entities = tracker.latest_message.get('entities', [])

    entities_obj = [e for e in entities]

    data = {
      'entities' : entities_obj,
      'intent' : intent
    }

    headers = {
      'Content-Type': 'application/json',
    }

    req = requests.post(url = route_config.get_route('action_subscribe'),headers= headers,data=json.dumps(data))

    dispatcher.utter_message(req.json())
    return