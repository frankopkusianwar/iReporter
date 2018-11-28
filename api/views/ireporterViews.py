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

@bp.route("/incidents/<int:incid_id>", methods=["GET"])
def get_specific_redflag(incid_id):
    return searchId(incid_id, incidents)

@bp.route("/incidents/<int:incid_id>/location", methods=["PATCH"])
def edit_specific_redflag_location(incid_id):
    return edit_incident(incid_id,incidents)

@bp.route("/incidents/<int:incid_id>/comment", methods=["PATCH"])
def add_comment_to_specific_redflag_record():
    pass

@bp.route("/incidents/<int:incid_id>", methods=["DELETE"])
def delete_specific_redflag_record(incid_id):
    return deleteId(incid_id, incidents)