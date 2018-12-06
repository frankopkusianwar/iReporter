from flask import request, Response, json, jsonify
from api.models.ireportermodels import BaseUser, User, IreporterDb
from api.utilities import make_id
import uuid
import datetime

new_user = IreporterDb()




class UserController:
    def create_user(self):
        user_data = request.get_json()
        user_id = make_id("userObject", new_user.user_list)
        first_name = user_data.get('firstName')
        last_name = user_data.get('lastName')
        other_names = user_data.get('otherNames')
        username = user_data.get('username')
        email = user_data.get('email')
        password = user_data.get('password')
        registered = datetime.datetime.today()
        is_admin = False

        user = User(BaseUser(other_names, username, password, registered),
        user_id, first_name, last_name, email, is_admin)
        
        new_user.add_user(user)

        return jsonify({
            "id": user_id,
            "status": 201,
            "message": "user created successfully", 
            "data": user.make_json()
        }), 201

    
'''class IncidentController:

    def add_red_flag(self):
        data = request.get_json()

        redflgs = [data["latitude"], data["longitude"], data["images"]]
        for rflg in redflgs:
            if not rflg :
                return jsonify({"status":200,"message": "Please fill in all the fields"})

            if type(rflg ) != str:
                return jsonify({"status":200,"message": "Please fields must contain string values"})
            
            if rflg.isspace():
                return jsonify({"status":200,"message": "Please fields must not be filled with a space "})

        RedFlag.created_by = request.headers["userId"]
        RedFlag.created_on = datetime.datetime.today()
        RedFlag.latitude = data['latitude']
        RedFlag.longitude = data['longitude']
        RedFlag.images = data['images']
        RedFlag.red_flag_incident_type = "red-flag"
        RedFlag.status = "draft"
        RedFlag.comment = ""
        if len(incidents) == 0: 
            RedFlag.incident_id = len(incidents)+1 
        else: 
            RedFlag.incident_id = incidents[-1]["incidentId"]+1

        incident_data = {
            "incidentId": RedFlag.incident_id,
            "createdOn": RedFlag.created_on,
            "createdBy": RedFlag.created_by,
            "latitude": RedFlag.latitude,
            "longitude": RedFlag.longitude,
            "images": RedFlag.images.split(","),
            "status": RedFlag.status,
            "incidentType": RedFlag.red_flag_incident_type,
            "comment": RedFlag.comment
            }
        incidents.append(incident_data)
        return jsonify({
                "data":incidents,
                "status":201,
                "id":incident_data['incidentId'],
                "message":"Incident created successully"
                })

    def add_intervention(self):
        data = request.get_json()

        intv = [data["latitude"], data["longitude"], data["images"]]
        for intv in intv:
            if not intv :
                return jsonify({"status":200,"message": "Please fill in all the fields"})

            if type(intv) != str:
                return jsonify({"status":200,"message": "Please fields must contain string values"})
            
            if intv.isspace():
                return jsonify({"status":200,"message": "Please fields must not be filled with a space "})

        Intervention.created_by = request.headers["userId"]
        Intervention.created_on = datetime.datetime.today()
        Intervention.latitude = data['latitude']
        Intervention.longitude = data['longitude']
        Intervention.images = data['images']
        Intervention.internention_incident_type = "intervention"
        Intervention.status = "draft"
        Intervention.comment = ""
        if len(incidents) == 0: 
            Intervention.incident_id = len(incidents)+1 
        else: 
            Intervention.incident_id = incidents[-1]["incidentId"]+1

        incident_data = {
            "incidentId": Intervention.incident_id,
            "createdOn": Intervention.created_on,
            "createdBy": Intervention.created_by,
            "latitude": Intervention.latitude,
            "longitude": Intervention.longitude,
            "images": Intervention.images.split(","),
            "status": Intervention.status,
            "incidentType": Intervention.internention_incident_type,
            "comment": Intervention.comment
            }
        incidents.append(incident_data)
        return jsonify({
                "data":incidents,
                "status":201,
                "id":incident_data['incidentId'],
                "message":"Incident created successully"
                })
    def get_all_incidents(self):
        if len(incidents) == 0:
            return jsonify({"status": 200, "message":"No incident records found"})
        return jsonify({
                    "status":201,
                    "data":incidents
                    })

    def get_specific_record(self,item_id, list_of_Items):
        item = [item for item in list_of_Items if item['incidentId'] == item_id]
        if len(item) == 0:
            return jsonify({"status":200,"message":"The incident id your trying to get does not exist"})
        return jsonify({
                    "status":200,
                    "id": item_id,
                    "data":item,
                    "message":"incident record returned successfully"
                    })

    def edit_incident(self,search_item, list_of_Items):
        item = [item for item in list_of_Items if item['incidentId'] == search_item]
        if len(item) == 0:
            return jsonify({"status":200,"message":"The record id your trying to update does not exist"})
        
        edit_data = request.get_json()
        latlong = [edit_data["latitude"], edit_data["longitude"]]
        for edit in latlong:
            if not edit :
                return jsonify({"status":200,"message": "Please fill in all the fields"})

            if type(edit) != str:
                 return jsonify({"status":200,"message": "Please fields must contain string values"})
                
            if edit.isspace():
                return jsonify({"status":200,"message": "Please fields must not be filled with a space "})
        item[0]['latitude'] = request.json.get('latitude', item[0]['latitude'])
        item[0]['longitude'] = request.json.get('longitude', item[0]['longitude'])

        return jsonify({
                        "status":200,
                        "id": search_item,
                        "data":incidents,
                        "message":"incident location updated successfully"})

    def edit_comment(self,comments_id, list_of_Items):
        item = [item for item in list_of_Items if item['incidentId'] == comments_id]
        if len(item) == 0:
            return jsonify({"status":200,"message":"The record id your trying to comment on does not exist"})
        
        comment_data = request.get_json()
        com = comment_data["comment"]

        if not com :
            return jsonify({"status":200,"message": "Please fill in the comment"})

        if type(com) != str:
            return jsonify({"status":200,"message": "Please comment must be a string value"})
                
        if com.isspace():
            return jsonify({"status":200,"message": "Please fields must not be filled with a space "})
        item[0]['comment'] = request.json.get('comment', item[0]['comment'])

        return jsonify({
                        "status":200,
                        "id": comments_id,
                        "data":incidents,
                        "message":"comment added successfully"})

    def deleteId(self,search_item, list_of_Items):
        item = [item for item in list_of_Items if item['incidentId'] == search_item]
        if len(item) == 0:
            return jsonify({"status":200,"message":"The record id your trying to delete does not exist"})
        list_of_Items.remove(item[0])
        return jsonify({
                    "status":200,
                    "id": search_item,
                    "data":incidents,
                    "message":"incident record deleted successfully"
                    })'''