from flask import Blueprint
from api.controllers.ireportercontrollers import UserController, IncidentController, incidents

bp = Blueprint("ireporterViews", __name__, url_prefix="/api/v1")
incidnt = IncidentController()
@bp.route("/users", methods=["POST"])
def createUser():
    us = UserController()
    return us.addUser()

@bp.route("/red-flags", methods=["POST"])
def create_red_flag_record():
    return incidnt.add_red_flag()

@bp.route("/interventions", methods=["POST"])
def create_intervention_record():
    incidnt = IncidentController()
    return incidnt.add_intervention()

@bp.route("/incidents", methods=["GET"])
def get_all_incidents_records():
    return incidnt.get_all_incidents()

@bp.route("/incidents/<int:incid_id>", methods=["GET"])
def get_specific_incident_record(incid_id):
    return incidnt.get_specific_record(incid_id, incidents)

@bp.route("/incidents/<int:incid_id>/location", methods=["PATCH"])
def edit_specific_incident_location(incid_id):
    return incidnt.edit_incident(incid_id,incidents)

@bp.route("/incidents/<int:incid_id>/comment", methods=["PATCH"])
def add_comment_to_specific_incident_record(incid_id):
    return incidnt.edit_comment(incid_id,incidents)

@bp.route("/incidents/<int:incid_id>", methods=["DELETE"])
def delete_specific_incident_record(incid_id):
    return incidnt.deleteId(incid_id, incidents)