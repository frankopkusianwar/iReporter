from flask import request, Response, json, jsonify
from api.models.ireportermodels import BaseIncident, Incident, IreporterDb
from api.utilities import make_id, check_empty
import uuid
import datetime

new_inc = IreporterDb()

class IncidentController:
    def create_incident(self):
        inc_data = request.get_json()
        incident_id = make_id("incObject", new_inc.incident_list)
        incident_type = inc_data.get('incidentType')
        location = inc_data.get('location')
        status = "draft"
        created_on = datetime.datetime.today()
        created_by = request.headers["userId"]
        images = inc_data.get('images')
        videos = inc_data.get('videos')
        comment = ""

        

        incident = Incident(BaseIncident(images, videos, created_on, created_by,comment),
        incident_id, incident_type, location, status)
        
        new_inc.add_incident(incident)

        return jsonify({
            "id": incident_id,
            "status": 201,
            "message": "incident created successfully", 
            "data": incident.incident_json()
        }), 201

    def get_inc(self):
        return jsonify({
            "status": 200,
            "data": new_inc.get_incidents()
        })

    def get_spec_inc(self, particular_id):
        if new_inc.get_specific_incident(particular_id) == None:
            return jsonify({"status":200,"message":"requested red-flag-id not found"})
        return jsonify({
            "status": 200,
            "data": new_inc.get_specific_incident(particular_id)
        })

    def del_spec_inc(self, del_id):
        if new_inc.delete_incident(del_id) == None:
            return jsonify({"status":200,"message":"the red-flag you're trying to delete does not exist"})
        return jsonify({
            "id": del_id,
            "status": 200,
            "data": new_inc.get_incidents(),
            "message": "red-flag deleted successfully"
        })
