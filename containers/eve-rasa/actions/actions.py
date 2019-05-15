import requests
import json
from api.api_config import ApiConfig
from rasa_core_sdk import Action

class SubscribeAction(Action):
  def name(self):
    return "action_subscribe"

  def run(self, dispatcher, tracker, domain):
    intent = tracker.latest_message["intent"].get("name")
    entities = tracker.latest_message.get("entities", [])
    # entity = {e["entity"]: e["value"] for e in entities}[0]

    if intent is None:
      intent = ""
    
    if len(entities) == 0:
      entities = []

    # url = ApiConfig().get_action_answer_URL()+ "?intent={}&entity={}".format(intent,entity)
    

    # entities_json = json.dumps(entities)
    # entity = getattr(domain,"entities").first()
    # intent = getattr(domain,"intents").first()
    # entity = tracker.latest_message["entities"][0]["value"]
    # entity = tracker.latest_message["entities"]
    # print(entity)
    # intent = tracker.latest_message["intent"]["name"]
    # r = requests.get(url)

    dispatcher.utter_message(intent) #send the message back to the user
    return