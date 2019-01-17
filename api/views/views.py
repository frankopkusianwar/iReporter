from flask import Blueprint, request
from api.controllers.userController import UserController
from api.controllers.incidentController import IncidentController

bp = Blueprint("ireporterViews", __name__, url_prefix="/api/v1")
incident = IncidentController()
user = UserController()

@bp.route("/users", methods=["POST"])
def createUser():
    return user.create_user()

@bp.route("/red-flags", methods=["GET","POST"])
def redFlags():
    if request.method == 'POST':
        return incident.create_incident()
    else:
        return incident.get_all_incident()

@bp.route("/red-flags/<int:red_flag_id>", methods=["GET","DELETE"])
def SpecificIncidents(red_flag_id):
    if request.method == 'GET':
        return incident.get_one_incident(red_flag_id)
    else:
        return incident.delete_one_incident(red_flag_id)

@bp.route("/red-flags/<int:location_incident_id>/location", methods=["PATCH"])
def edit_specific_incident_location(location_incident_id):
    return incident.update_particular_location(location_incident_id)

@bp.route("/red-flags/<int:comment_incident_id>/comment", methods=["PATCH"])
def add_comment_to_specific_red_flag_record(comment_incident_id):
    return incident.create_comment(comment_incident_id)

@bp.route("/red-flags/<int:status_incident_id>/status", methods=["PATCH"])
def change_red_flag_status(status_incident_id):
    return incident.change_particular_status(status_incident_id)