from flask import json
import unittest
from api.models.ireportermodels import User, users, Incident, incidents, RedFlag, Intervention
from api import app
from flask import json

class TestEndpts(unittest.TestCase):
    def setUp(self):
        self.test_client = app.test_client(self)

    def test_create_user(self):
        userData = {

        "firstName": "frank",
        "lastName": "okiror",
        "otherNames": "of",
        "userName": "franko",
        "email": "okirorfrank3@gmailcom",
        "password": "1234",
        }
        response = self.test_client.post(
            'api/v1/users',
            content_type='application/json',
            data=json.dumps(userData)
        )
        message = json.loads(response.data.decode())

        self.assertEqual(message['message'],
                         'user created successully')
        
        self.assertEqual(message['status'],
                            201)
        userlen = len(users)
        users.append(userData)
        assert(len(users) > userlen)
    
    def test_add_red_flag(self):
        red_flag_data = {
            "incidentId": 2,
            "createdOn": "24-nov-2018",
            "createdBy": 1,
            "latitude": "23.00",
            "longitude": "43.00",
            "images": "images,images",
            "status": "draft",
            "incidentType": "red-flag",
            "comment": ""
        }

        response = self.test_client.post(
            'api/v1/red-flags',
            content_type='application/json',
            data=json.dumps(red_flag_data)
        )
        #message = json.loads(response.data.decode())
