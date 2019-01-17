from flask import request, jsonify
from api.models.models import Incident, IreporterDb
from api.utilities import make_id, check_inc
import uuid
import datetime

new_incident = IreporterDb()

class IncidentController:
    def create_incident(self):
        incident_data = request.get_json()
        incident_id = make_id("incObject", new_incident.incident_list)
        incident_type = incident_data.get('incidentType')
        location = incident_data.get('location')
        status = "draft"
        created_on = datetime.datetime.today()
        created_by = request.headers["userId"]
        images = incident_data.get('images')
        videos = incident_data.get('videos')
        comment = ""
        public_incident_id = str(uuid.uuid4())
        validate_fields = [location, images, videos]
        if check_inc(validate_fields,location,images,videos) == "invalid":
            return jsonify({"status": 400, "message":"please fill all fields"}),400
        if incident_type != "red-flag" and incident_type != "intervention":
            return jsonify({"status":400,"message":"please enter incidentType as red-flag or intervention"}),400

        
        incident = Incident(incident_id, incident_type, location, status, images, videos, created_on, created_by,comment, public_incident_id)
        
        new_incident.add_incident(incident)

        return jsonify({
            "data": [{
            "id": incident_id,
            "status": 201,
            "message": "created red-flag record", 
            }]
        }), 201

    def get_all_incident(self):
        if new_incident.get_incidents() == None:
            return jsonify({"status":200,"message":"red-flag records not found"})
        return jsonify({
            "status": 200,
            "data": new_incident.get_incidents()
        })

    def get_one_incident(self, particular_id):
        if new_incident.get_specific_incident(particular_id) == None:
            return jsonify({"status":200,"message":"requested red-flag-id not found"})
        return jsonify({
            "status": 200,
            "data": [new_incident.get_specific_incident(particular_id)]
        })

    def delete_one_incident(self, delete_id):
        if new_incident.delete_incident(delete_id) == None:
            return jsonify({"status":200,"message":"the id to delete does not exist or status is under investigation, rejected, or resolved"})
        return jsonify({
            "data": [{
            "id": delete_id,
            "status": 200,
            "message": "red-flag record has been deleted"
            }]
        })

    def create_comment(self, comment_id):
        comment_data = request.get_json()
        new_comment = comment_data.get("comment")
        if new_incident.add_comment(comment_id,new_comment) == None:
            return jsonify({"status":200,"message":"the red-flag you're trying to comment on  does not exist"})
        return jsonify({
            "data": [{
            "id": comment_id,
            "status":200,
            "message": "updated red-flag record's comment"
            }]
        })   

    def update_particular_location(self, location_id):
        location_data = request.get_json()
        new_location = location_data.get("location")
        if new_incident.edit_red_flag(location_id,new_location) == None:
            return jsonify({"status":200,"message":"the id does not exist or status is under investigation, rejected, or resolved"})
        return jsonify({
            "data": [{
            "id": location_id,
            "status":200,
            "message": "updated red-flag record's location"
            }]
        })
        
    def change_particular_status(self, status_id):
        status_data = request.get_json()
        new_status = status_data.get("status")
        if new_incident.update_status(status_id,new_status) == None:
            return jsonify({"status":200,"message":"the red-flag you're trying to change status does not exist"})
        return jsonify({
            "id": status_id,
            "status":200,
            "data": new_incident.get_specific_incident(status_id),
            "message": "status updated successfully"
        })