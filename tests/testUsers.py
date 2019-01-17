import unittest
from api.models.models import User, Incident, IreporterDb
from api import app
from flask import request
import json

class TestUsers(unittest.TestCase):
    def setUp(self):
        self.test_client = app.test_client(self)

    def test_create_user(self):
        user = User("of", "franko", "123456789", "25-nov-2018", 2, "frank", "okiror", "okirorfrank3@gmail.com", False, "fgfhfhf768sus88")
        user_data = user.make_json()
        response = self.test_client.post(
            'api/v1/users',
            content_type='application/json',
            data=json.dumps(user_data)
        )
        message = json.loads(response.data.decode())
        self.assertEqual(message['data'][0]['message'],
                         'user created successfully')

    def test_user_empty_fields(self):
        user = User("", "", "123456789", "25-nov-2018", 2, "frank", "okiror", "okirorfrank3@gmail.com", False, "fgfhfhf768sus88")
        user_data = user.make_json()
        response = self.test_client.post(
            'api/v1/users',
            content_type='application/json',
            data=json.dumps(user_data)
        )
        message = json.loads(response.data.decode())
        self.assertEqual(message['message'],
                         'please fill all fields')

    def test_for_valid_email(self):
        user = User("frank", "of", "123456789", "25-nov-2018", 2, "frank", "okiror", "okirorfrankgmail.com", False, "fgfhfhf768sus88")
        user_data = user.make_json()
        response = self.test_client.post(
            'api/v1/users',
            content_type='application/json',
            data=json.dumps(user_data)
        )
        message = json.loads(response.data.decode())
        self.assertEqual(message['message'],
                         'invalid email adress')

    def test_check_password_length(self):
        user = User("frank", "of", "123", "25-nov-2018", 2, "frank", "okiror", "okirorfrank3@gmail.com", False, "fgfhfhf768sus88")
        user_data = user.make_json()
        response = self.test_client.post(
            'api/v1/users',
            content_type='application/json',
            data=json.dumps(user_data)
        )
        message = json.loads(response.data.decode())
        self.assertEqual(message['message'],
                         'password should be more than 8 characters')      