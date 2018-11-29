from flask import request, Response, json, jsonify
from api.models.ireportermodels import User, users, Incident, incidents, RedFlag, Intervention
from api.utilities import *
import uuid
import datetime

def addUser():
    request_data = request.get_json()

    if check_for_empty_fields(request_data["firstName"], request_data["lastName"], request_data["otherNames"], 
                                request_data["userName"], request_data["email"], request_data["password"]):
        return jsonify({"status":200,"message": "Please fill in all the fields"})

    if check_for_string_input(request_data["firstName"], request_data["lastName"], request_data["otherNames"], 
                                request_data["userName"], request_data["email"], request_data["password"]):
        return jsonify({"status":200,"message": "Please fields must contain string values"})

    if check_for_space(request_data["firstName"], request_data["lastName"], request_data["otherNames"], 
                                request_data["userName"], request_data["email"], request_data["password"]):
        return jsonify({"status":200,"message": "Please fields must not be filled with a space "})

    user = User()
    user.first_name = request_data["firstName"]
    user.last_name = request_data["lastName"]
    user.other_names = request_data["otherNames"]
    user.user_name = request_data["userName"]
    user.email = request_data["email"]
    user.password = request_data["password"]
    user.registered = datetime.datetime.today()


    def addUserId():
        if len(users) == 0: 
            user_id = len(users)+1 
        else: 
            user_id = users[-1]["userId"]+1
        return user_id

    usersData = {
        "userId": addUserId(),
        "firstName": user.first_name,
        "lastName": user.last_name,
        "otherNames": user.other_names,
        "userName": user.user_name,
        "email": user.email,
        "password": user.password,
        "registered": user.registered,
        "public_userId": str(uuid.uuid4())
        }
    users.append(usersData)
    return jsonify({
                    "data":users,
                    "status":201,
                    "id":usersData['userId'],
                    "message":"user created successully"
                    })

inc = Incident()

def addIncident():
    request_data = request.get_json()
    
    inc.created_by = request.headers["userId"]
    inc.created_on = datetime.datetime.today()
    inc.latitude = request_data["latitude"]
    inc.longitude = request_data["longitude"]
    inc.images = request_data["images"].split(",")
    inc.status = "draft"

def add_incident_id():
    if len(incidents) == 0: 
        incident_id = len(incidents)+1 
    else: 
        incident_id = incidents[-1]["incidentId"]+1
    return incident_id
        

def add_red_flag():
    red = RedFlag()
    addIncident()

    incident_data = {
            "incidentId": add_incident_id(),
            "createdOn": inc.created_on,
            "createdBy": inc.created_by,
            "incidentType": red.red_flag_incident_type,
            "latitude": inc.latitude,
            "longitude": inc.longitude,
            "images": inc.images,
            "status": inc.status,
            "comment": ""
            }
    incidents.append(incident_data)
    return jsonify({
            "data":incidents,
            "status":201,
            "id":incident_data['incidentId'],
            "message":"Incidents created successully"
            })

def add_intervention():
    intv = Intervention()
    addIncident()

    incident_data = {
            "incidentId": add_incident_id(),
            "createdOn": inc.created_on,
            "createdBy": inc.created_by,
            "incidentType": intv.internention_incident_type,
            "latitude": inc.latitude,
            "longitude": inc.longitude,
            "image": inc.images,
            "status": inc.status,
            "comment": ""
            }
    incidents.append(incident_data)
    return jsonify({
            "data":incidents,
            "status":201,
            "id":incident_data['incidentId'],
            "message":"Incident created successully"
            })


def getAllIncidents():
    if len(incidents) == 0:
        return jsonify({"status": 200, "message":"No incident records found"})
    return jsonify({
                    "status":201,
                    "data":incidents
                    })

def searchId(search_item, list_of_Items):
    search_list = []
    for item in list_of_Items:
        for key in item:
            if item[key] == search_item:
                search_list.append(item)
    if len(search_list) == 0:
        return jsonify({"message":"incident id does not exist"})            
    return jsonify({
                    "status":201,
                    "data":search_list
                    })

def deleteId(search_item, list_of_Items):
    item = [item for item in list_of_Items if item['incidentId'] == search_item]
    if len(item) == 0:
        return jsonify({"status":200,"message":"The record id your trying to delete does not exist"})
    list_of_Items.remove(item[0])
    return jsonify({
                    "status":200,
                    "id": search_item,
                    "data":incidents,
                    "message":"red-flag record deleted successfully"
                    })
def edit_incident(search_item, list_of_Items):
    item = [item for item in list_of_Items if item['incidentId'] == search_item]
    if len(item) == 0:
        return jsonify({"status":200,"message":"The record id your trying to update does not exist"})
    
    
    request_data = request.get_json()
    if check_for_empty_fields(request_data["latitude"],request_data["longitude"]):
        return jsonify({"status":200,"message": "Please fill in all fields field"})

    if check_for_string_input(request_data["latitude"],request_data["longitude"]):
        return jsonify({"status":200,"message": "Please latitude and longitude should be a string"})

    if check_for_space(request_data["latitude"],request_data["longitude"]):
        return jsonify({"status":200,"message": "Please enter latitude and logitude co-ordinates not spaces"})


    item[0]['latitude'] = request.json.get('latitude', item[0]['latitude'])
    item[0]['longitude'] = request.json.get('longitude', item[0]['longitude'])

    return jsonify({
                    "status":200,
                    "id": search_item,
                    "data":incidents,
                    "message":"red-flag location updated successfully"
                    })

def add_comment(search_item, list_of_Items):
    item = [item for item in list_of_Items if item['incidentId'] == search_item]

    if len(item) == 0:
        return jsonify({"status":200,"message":"The record id your trying to comment on does not exist"})

    request_data = request.get_json()
    if check_for_empty_fields(request_data["comment"]):
        return jsonify({"status":200,"message": "Please fill in the comment field"})

    if check_for_string_input(request_data["comment"]):
        return jsonify({"status":200,"message": "Please comment shouled be a string"})

    if check_for_space(request_data["comment"]):
        return jsonify({"status":200,"message": "Please space input is not allowed in comments"})
    
    item[0]['comment'] = request.json.get('comment', item[0]['comment'])

    return jsonify({
                    "status":200,
                    "id": search_item,
                    "data":incidents,
                    "message":"incident commment added successfully"
                    })
