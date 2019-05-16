import requests
import json
from api.route_config import RouteConfig
from rasa_core_sdk import Action

route_config = RouteConfig('5000','eve_api')
#register route actions
route_config.register_route('action-answer','/action-answer')

class SubscribeAction(Action):
  def name(self):
    return "action_subscribe"

  def run(self, dispatcher, tracker, domain):
    intent = tracker.latest_message['intent'].get('name')
    entities = tracker.latest_message.get('entities', [])
    obj_entities = []
    for e in entities:
      obj_entities.append(e['value'])

    data = {
      'entities' : obj_entities,
      'intent' : intent
    }

    headers = {
      'Content-Type': 'application/json',
    }

    req = requests.post(url = route_config.get_route('action-answer'),headers= headers,data=json.dumps(data))

    dispatcher.utter_message(req.json())
    return