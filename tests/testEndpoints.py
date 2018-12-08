from flask import json
import unittest
from api.models.ireportermodels import BaseUser, User, BaseIncident, Incident, IreporterDb
from api import app
from flask import json

class TestEndpts(unittest.TestCase):
    def setUp(self):
        self.test_client = app.test_client(self)

    def test_create_user(self):
        user = User(BaseUser("of", "franko", "123456789", "25-nov-2018"),
        "2", "frank", "okiror", "okirorfrank3@gmail.com", False)
        user_data = user.make_json()
        response = self.test_client.post(
            'api/v1/users',
            content_type='application/json',
            data=json.dumps(user_data)
        )
        message = json.loads(response.data.decode())

        self.assertEqual(message['message'],
                         'user created successfully')
        
        self.assertEqual(message['status'],
                            201)
    
    
