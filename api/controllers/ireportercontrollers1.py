from flask import request, Response, jsonify
from api.models.models import BaseIncident, Incident, IreporterDb
from api.utilities import make_id, check_inc
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
        val_fields = [location, images, videos]
        if check_inc(val_fields,location,images,videos) == "invalid":
            return jsonify({"status": 400, "message":"please fill all fields"}),400
        if incident_type != "red-flag" and incident_type != "intervention":
            return jsonify({"status":400,"message":"please enter incidentType as red-flag or intervention"}),400

        incident = Incident(BaseIncident(images, videos, created_on, created_by,comment),
        incident_id, incident_type, location, status)
        
        new_inc.add_incident(incident)

        return jsonify({
            "data": [{
            "id": incident_id,
            "status": 201,
            "message": "created red-flag record", 
            }]
        }), 201

    def get_inc(self):
        if new_inc.get_incidents() == None:
            return jsonify({"status":200,"message":"red-flag records not found"})
        return jsonify({
            "status": 200,
            "data": new_inc.get_incidents()
        })

    def get_spec_inc(self, particular_id):
        if new_inc.get_specific_incident(particular_id) == None:
            return jsonify({"status":200,"message":"requested red-flag-id not found"})
        return jsonify({
            "status": 200,
            "data": [new_inc.get_specific_incident(particular_id)]
        })

    def del_spec_inc(self, del_id):
        if new_inc.delete_incident(del_id) == None:
            return jsonify({"status":200,"message":"the id to delete does not exist or status is under investigation, rejected, or resolved"})
        return jsonify({
            "data": [{
            "id": del_id,
            "status": 200,
            "message": "red-flag record has been deleted"
            }]
        })

    def create_comment(self, comm_id):
        com_data = request.get_json()
        new_comment = com_data.get("comment")
        if new_inc.add_comment(comm_id,new_comment) == None:
            return jsonify({"status":200,"message":"the red-flag you're trying to comment on  does not exist"})
        return jsonify({
            "data": [{
            "id": comm_id,
            "status":200,
            "message": "updated red-flag record's comment"
            }]
        })   

    def update_loc(self, loc_id):
        loc_data = request.get_json()
        new_loc = loc_data.get("location")
        if new_inc.edit_red_flag(loc_id,new_loc) == None:
            return jsonify({"status":200,"message":"the id does not exist or status is under investigation, rejected, or resolved"})
        return jsonify({
            "data": [{
            "id": loc_id,
            "status":200,
            "message": "updated red-flag record's location"
            }]
        })
        
    def chng_status(self, st_id):
        st_data = request.get_json()
        new_st = st_data.get("status")
        if new_inc.update_status(st_id,new_st) == None:
            return jsonify({"status":200,"message":"the red-flag you're trying to change status does not exist"})
        return jsonify({
            "id": st_id,
            "status":200,
            "data": new_inc.get_specific_incident(st_id),
            "message": "status updated successfully"
        })