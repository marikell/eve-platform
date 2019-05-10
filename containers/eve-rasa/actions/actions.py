import requests
import json
from rasa_core_sdk import Action

class SubscribeAction(Action):
  def name(self):
    return "action_subscribe"

  def run(self, dispatcher, tracker, domain):
    text = 'Okay! Now you are subscribed'
    dispatcher.utter_message(text) #send the message back to the user
    return []