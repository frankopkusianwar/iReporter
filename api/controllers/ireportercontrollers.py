from flask import request, Response, json, jsonify
from api.models.ireportermodels import User, users, Incident, incidents, RedFlag, Intervention
import uuid
import datetime

def addUser():
    request_data = request.get_json()
    
    user = User()
    user.first_name = request_data["firstName"]
    user.Last_name = request_data["lastName"]
    user.other_names = request_data["otherNames"]
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
    
    inc.latitude = request_data["latitude"]
    inc.longitude = request_data["longitude"]
    inc.images = request_data["images"]

def add_incident_id():
    if len(incidents) == 0: 
        incident_id = len(incidents)+1 
    else: 
        incident_id = incidents[-1]["incidentId"]+1
    return incident_id
        

def add_red_flag():
    red = RedFlag()
    addIncident()
    crtd = request.headers["userId"]

    incident_data = {
            "incidentId": add_incident_id(),
            "createdOn": datetime.datetime.today(),
            "createdBy": crtd,
            "incidentType": red.red_flag_incident_type,
            "latitude": inc.latitude,
            "longitude": inc.longitude,
            "image": inc.images.split(","),
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

def add_intervention():
    intv = Intervention()
    addIncident()
    crtd = request.headers["userId"]

    incident_data = {
            "incidentId": add_incident_id(),
            "createdOn": datetime.datetime.today(),
            "createdBy": crtd,
            "incidentType": intv.internention_incident_type,
            "latitude": inc.latitude,
            "longitude": inc.longitude,
            "image": inc.images.split(","),
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
    return jsonify({
                    "status":201,
                    "data":incidents
                    })

def searchId(search_item, list_of_Items):
    search_list = []
    for item in list_of_Items:
        [search_list.append(item) for key in item if item[key] == search_item]
    return jsonify({
                    "status":201,
                    "data":search_list
                    })

def deleteId(search_item, list_of_Items):
    for item in list_of_Items:
        [list_of_Items.remove(item) for key in item if item[key] == search_item]
    return jsonify({
                    "status":200,
                    "id": search_item,
                    "data":incidents,
                    "message":"red-flag record deleted successfully"
                    })
def edit_incident(search_item, list_of_Items):
    item = [item for item in list_of_Items if item['incidentId'] == search_item]
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
    item[0]['comment'] = request.json.get('comment', item[0]['comment'])

    return jsonify({
                    "status":200,
                    "id": search_item,
                    "data":incidents,
                    "message":"incident commment added successfully"
                    })