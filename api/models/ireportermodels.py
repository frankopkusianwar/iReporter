from flask import jsonify
class BaseUser:
    """model class for user"""
    def __init__(self, other_names, username, password, registered):
        self.other_names = other_names
        self.user_name = username
        self.password = password
        self.registered = registered

class User:
    def __init__(self, base, user_id, first_name, last_name, email, is_admin):
        self.base = base
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin

    def make_json(self):
        info ={
            "Id": self.user_id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "otherNames": self.base.other_names,
            "email": self.email,
            "username": self.base.user_name,
            "registered": self.base.registered,
            "password": self.base.password,
            "isAdmin": self.is_admin
        }
        return info

class BaseIncident:
    """model class for incidents"""
    def __init__(self, images, videos, created_on, created_by, comment):
        self.images = images
        self.videos = videos
        self.created_on = created_on
        self.created_by = created_by
        self.comment = comment

class Incident:
    def __init__(self, base, incident_id, incident_type, location, status):
        self.base = base
        self.incident_id = incident_id
        self.incident_type = incident_type
        self.location = location
        self.status = status

    def incident_json(self):
        incident_info ={
            "id": self.incident_id,
            "createdOn": self.base.created_on,
            "createdBy": self.base.created_by,
            "type": self.incident_type,
            "location": self.location,
            "status": self.status,
            "images": self.base.images,
            "videos": self.base.videos,
            "comment": self.base.comment
        }
        return incident_info

class IreporterDb:
    def __init__(self):
        
        self.user_list = []
        self.incident_list = []

    def add_user(self, user_item):
        self.user_list.append(user_item)

    def add_incident(self, incident_item):
        self.incident_list.append(incident_item)

    def get_incidents(self):
        if len(self.incident_list) == 0:
            return None 
        return [incidents.incident_json() for incidents in self.incident_list]
    
    def get_specific_incident(self, return_id):
        for incident in self.incident_list:
             if incident.incident_id == return_id:
                return incident.incident_json() 
        return None
    
    def delete_incident(self, delete_id):
        for del_incident in self.incident_list:
             if del_incident.incident_id == delete_id and del_incident.status == "draft":
                 self.incident_list.remove(del_incident)
                 return "deleted"    
        return None

    def add_comment(self, comment_id, comm):
        for com in self.incident_list:
             if com.incident_id == comment_id:
                 com.base.comment = comm
                 return "comment added"  
        return None
    
    def edit_red_flag(self, location_id, locatn):
        for loc in self.incident_list:
             if loc.incident_id == location_id and loc.status == "draft":
                 loc.location = locatn
                 return "location updated"  
        return None

    def update_status(self, status_id, stat):
        for st in self.incident_list:
             if st.incident_id == status_id:
                 st.status = stat
                 return "status updated"  
        return None

        
