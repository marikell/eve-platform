from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import requests
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from bag_of_words import calculate_similarity

class GetAnswer(Action):
    def name(self):
        return "get_question_answer"
    def run(self, dispatcher, tracker, domain):
        print(tracker.latest_message)
        question = tracker.latest_message['text']
        response = calculate_similarity(question)
        dispatcher.utter_message(response)