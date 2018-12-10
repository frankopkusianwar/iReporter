import unittest
from api.models.ireportermodels import BaseUser, User, BaseIncident, Incident, IreporterDb
from api import app
from flask import request
import json


class TestEndpoints(unittest.TestCase):
    def setUp(self):
        self.test_client = app.test_client(self)

    def test_create_user(self):
        user = User(BaseUser("of", "franko", "123456789", "25-nov-2018"),
        2, "frank", "okiror", "okirorfrank3@gmail.com", False)
        user_data = user.make_json()

        response = self.test_client.post(
            'api/v1/users',
            content_type='application/json',
            data=json.dumps(user_data)
        )
        message = json.loads(response.data.decode())

        self.assertEqual(message['message'],
                         'user created successfully')

    def test_user_empty_fields(self):
        user = User(BaseUser("", "", "123456789", "25-nov-2018"),
        2, "frank", "okiror", "okirorfrank3@gmail.com", False)
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
        user = User(BaseUser("frank", "of", "123456789", "25-nov-2018"),
        2, "frank", "okiror", "okirorfrankgmail.com", False)
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
        user = User(BaseUser("frank", "of", "123", "25-nov-2018"),
        2, "frank", "okiror", "okirorfrank3@gmail.com", False)
        user_data = user.make_json()

        response = self.test_client.post(
            'api/v1/users',
            content_type='application/json',
            data=json.dumps(user_data)
        )
        message = json.loads(response.data.decode())

        self.assertEqual(message['message'],
                         'password should be more than 8 characters')

    def test_create_incident(self):
        incident = Incident(BaseIncident(['images','image'], ['videos','videos'], "25-nov-2018", 2, "comment"),
            1, "red-flag", {"latitude":"120.00","longitude":"120.00"}, "draft")
        incident_data = incident.incident_json()

        response = self.test_client.post(
            'api/v1/red-flags',
            content_type='application/json',
            data=json.dumps(incident_data),
            headers={"userId": 2}
        )
        
        message = json.loads(response.data.decode())

        self.assertEqual(message['message'],
                         'red-flag created successfully')

    def test_check_invalid_incident_type(self):
        incident = Incident(BaseIncident(['images','images'], ['videos','videos'], "25-nov-2018", 2, "comment"),
            1, "invalid-type", {"latitude":"120.00","longitude":"120.00"}, "draft")
        incident_data = incident.incident_json()

        response = self.test_client.post(
            'api/v1/red-flags',
            content_type='application/json',
            data=json.dumps(incident_data),
            headers={"userId": 2}
        )
        
        message = json.loads(response.data.decode())

        self.assertEqual(message['message'],
                         'please enter incidentType as red-flag or intervention')

    def test_check_empty_incident_fields(self):
        incident = Incident(BaseIncident("", "", "", 2, ""),
            1, "invalid-type", "", "")
        incident_data = incident.incident_json()

        response = self.test_client.post(
            'api/v1/red-flags',
            content_type='application/json',
            data=json.dumps(incident_data),
            headers={"userId": 2}
        )
        
        message = json.loads(response.data.decode())

        self.assertEqual(message['message'],
                         'please fill all fields')

    def test_get_all_incidents(self):
        response = self.test_client.get('api/v1/red-flags')
        message = json.loads(response.data.decode())
        self.assertEqual(message['status'],
                         200)


