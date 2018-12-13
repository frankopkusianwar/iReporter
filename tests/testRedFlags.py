import unittest
from api.models.ireportermodels import BaseUser, User, BaseIncident, Incident, IreporterDb
from api import app
from flask import request
import json

class TestEndpoints(unittest.TestCase):
    def setUp(self):
        self.test_client = app.test_client(self)

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
        incident = Incident(BaseIncident(['images','image'], ['videos','videos'], "25-nov-2018", 2, "comment"),
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
                         
    #check for getting single red-flag record                     
    def test_get_single_red_flag(self):
        response = self.test_client.get('api/v1/red-flags/{}'.format(1))
        message = json.loads(response.data.decode())
        self.assertEqual(message['status'],
                         200)

    #test whether a comment is added osuccessfully
    def test_add_comment_to_red_flag(self):
        incident = Incident(BaseIncident(['images','image'], ['videos','videos'], "25-nov-2018", 2, "comment"),
            1, "red-flag", {"latitude":"120.00","longitude":"120.00"}, "draft")
        inc_data = incident.incident_json()
        self.test_client.post(
            'api/v1/red-flags',
            content_type='application/json',
            data=json.dumps(inc_data),
            headers={"userId": 2}
        ) 
        response = self.test_client.patch('api/v1/red-flags/{}/comment'.format(1), content_type='application/json', data=json.dumps({"comment":"this is a comment"}))
        message = json.loads(response.data.decode())
        self.assertEqual(message['message'],
                         'comment added successfully')

    def test_update_location(self):
        resp = self.test_client.patch('api/v1/red-flags/{}/location'.format(1), content_type='application/json', data=json.dumps({"location":{"latitude":"13.00","longitude":"13.00"}}))
        assert(resp.status_code) == 200
        message = json.loads(resp.data.decode())
        self.assertEqual(message['message'],
                         'location updated successfully')

    def test_update_status(self):
        resp = self.test_client.patch('api/v1/red-flags/{}/status'.format(1), content_type='application/json', data=json.dumps({"location":"resolved"}))
        assert(resp.status_code) == 200
        message = json.loads(resp.data.decode())
        self.assertEqual(message['message'],
                         'status updated successfully')

    def test_delete_red_flag(self):
        response = self.test_client.delete('api/v1/red-flags/{}'.format(2))
        message = json.loads(response.data.decode())
        self.assertEqual(message['message'],
                         'red-flag deleted successfully')

    #check for a red-flag id that does not exist
    def test_check_specific_red_flag_does_not_exist(self): 
        response = self.test_client.get('api/v1/red-flags/{}'.format(2))
        message = json.loads(response.data.decode())
        self.assertEqual(message['message'],
                         'requested red-flag-id not found') 

    def test_add_comment_id_does_not_exist(self): 
        response = self.test_client.patch('api/v1/red-flags/{}/comment'.format(2), content_type='application/json', data=json.dumps({"comment":"this is a comment"}))
        message = json.loads(response.data.decode())
        self.assertEqual(message['message'],
                         "the red-flag you're trying to comment on  does not exist")

    def test_check_delete_id_does_not_exist(self):
        response = self.test_client.delete('api/v1/red-flags/{}'.format(2))
        message = json.loads(response.data.decode())
        self.assertEqual(message['message'],
                         'the id to delete does not exist or status is under investigation, rejected, or resolved')

    def test_update_location_id_does_not_exist(self):
        resp = self.test_client.patch('api/v1/red-flags/{}/location'.format(2), content_type='application/json', data=json.dumps({"location":{"latitude":"13.00","longitude":"13.00"}}))
        assert(resp.status_code) == 200
        message = json.loads(resp.data.decode())
        self.assertEqual(message['message'],
                         'the id does not exist or status is under investigation, rejected, or resolved')

    def test_update_status_id_does_not_exist(self):
        resp = self.test_client.patch('api/v1/red-flags/{}/status'.format(2), content_type='application/json', data=json.dumps({"location":"resolved"}))
        assert(resp.status_code) == 200
        message = json.loads(resp.data.decode())
        self.assertEqual(message['message'],
                         "the red-flag you're trying to change status does not exist")                   
    