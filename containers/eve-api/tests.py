from app import flask_app
from api.models.answer import Answer
from mongoengine import connect
import json
import unittest
from api.config.configuration import ROUTE_CONFIG
from api.blueprints import answer_blueprint
from api.blueprints import entity_intent_answer_blueprint

class EveApiTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        
        # flask_app.config['MONGODB_SETTINGS'] = {
        #     'db': 'mongoenginetest',
        #     'host':'mongomock://localhost'
        # }

        flask_app.config['MONGODB_SETTINGS'] = {
            'db': 'evedb_test',
            'host':'mongodb://localhost:27017/evedb_test'
        }

        flask_app.testing = True

        flask_app.register_blueprint(answer_blueprint.app_answer)
        flask_app.register_blueprint(entity_intent_answer_blueprint.app_entity_intent_answer)

        self.app = flask_app.test_client()


    def test_ifFlaskIsRunning(self):
        
        response = self.app.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Flask is running in port 5001')
    
    def test_ifAnswerBlueprintIsRegisteredAndRunning(self):
        
        response = self.app.get('/api/answer')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello answer')

    def test_ifEntityIntentAnswerBlueprintIsRegisteredAndRunning(self):
        
        response = self.app.get('/api/entity-intent-answer')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello entity-intent-answer')
    
    def test_insertAnswerWithText(self):
        
        obj = {
            "text" : "teste01"
        }

        response=self.app.post('/api/answer', 
                       data=json.dumps(dict(text='oieeee')),
                       content_type='application/json')

        print(response.get_json())
        print(json.dumps(obj))

        self.assertEqual(response.get_json()['status'], 201)
        # self.assertEqual(response.get_json()['response'], '')
        # self.assertEqual(response.get_json()['response'], '')

    @classmethod
    def tearDownClass(self):
        self.oi = 'oi'