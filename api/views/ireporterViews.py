from flask import Blueprint
from api.controllers.ireportercontrollers import addUser, add_red_flag, add_intervention, getAllIncidents, searchId, incidents, deleteId, edit_incident

bp = Blueprint("ireporterViews", __name__, url_prefix="/api/v1")

@bp.route("/users", methods=["POST"])
def createUser():
    return addUser()

@bp.route("/red-flags", methods=["POST"])
def create_red_flag_record():
    return add_red_flag()

@bp.route("/interventions", methods=["POST"])
def create_intervention_record():
    return add_intervention()

@bp.route("/incidents", methods=["GET"])
def get_all_incident_records():
    return getAllIncidents()

@bp.route("/red-flags/<int:red_flag_id>", methods=["GET"])
def get_specific_redflag(red_flag_id):
    return searchId(red_flag_id, incidents)

@bp.route("/red-flags/<int:red_flag_id>/location", methods=["PATCH"])
def edit_specific_redflag_location(red_flag_id):
    return edit_incident(red_flag_id,incidents)

@bp.route("/red-flags/<int:red_flag_id>/comment", methods=["PATCH"])
def add_comment_to_specific_redflag_record():
    pass

@bp.route("/red-flags/<int:red_flag_id>", methods=["DELETE"])
def delete_specific_redflag_record(red_flag_id):
    return deleteId(red_flag_id, incidents)