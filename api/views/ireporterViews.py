from flask import Blueprint
from api.controllers.ireportercontrollers import UserController
from api.controllers.ireportercontrollers1 import IncidentController

bp = Blueprint("ireporterViews", __name__, url_prefix="/api/v1")
incdnt = IncidentController()

@bp.route("/users", methods=["POST"])
def createUser():
    us = UserController()
    return us.create_user()

@bp.route("/red-flags", methods=["POST"])
def createIcident():
    incdnt = IncidentController()
    return incdnt.create_incident()

@bp.route("/red-flags", methods=["GET"])
def getIncidents():
    incdnt = IncidentController()
    return incdnt.get_inc()

@bp.route("/red-flags/<int:red_flag_id>", methods=["GET"])
def getSpecificIncidents(red_flag_id):
    incdnt = IncidentController()
    return incdnt.get_spec_inc(red_flag_id)

@bp.route("/red-flags/<int:incid_id>/location", methods=["PATCH"])
def edit_specific_incident_location(incid_id):
    return incdnt.update_loc(incid_id)

@bp.route("/red-flags/<int:incid_id>/comment", methods=["PATCH"])
def add_comment_to_specific_red_flag_record(incid_id):
    return incdnt.create_comment(incid_id)

@bp.route("/red-flags/<int:incid_id>", methods=["DELETE"])
def delete_specific_incident_record(incid_id):
    return incdnt.del_spec_inc(incid_id)

@bp.route("/red-flags/<int:incid_id>/status", methods=["PATCH"])
def change_red_flag_status(incid_id):
    return incdnt.chng_status(incid_id)