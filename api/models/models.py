class User:
    """model class for user"""
    def __init__(self, other_names, username, password, registered, user_id, first_name, last_name, email, is_admin, public_user_id):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.other_names = other_names
        self.user_name = username
        self.password = password
        self.registered = registered
        self.public_user_id = public_user_id

    def make_json(self):
        info ={
            "Id": self.user_id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "otherNames": self.other_names,
            "email": self.email,
            "username": self.user_name,
            "registered": self.registered,
            "password": self.password,
            "isAdmin": self.is_admin,
            "publicUserId": self.public_user_id
        }
        return info

class Incident:
    def __init__(self,incident_id, incident_type, location, status, images, videos, created_on, created_by, comment, public_incident_id):
        self.incident_id = incident_id
        self.incident_type = incident_type
        self.location = location
        self.status = status
        self.images = images
        self.videos = videos
        self.created_on = created_on
        self.created_by = created_by
        self.comment = comment
        self.public_incident_id = public_incident_id

    def incident_json(self):
        incident_info ={
            "id": self.incident_id,
            "createdOn": self.created_on,
            "createdBy": self.created_by,
            "incidentType": self.incident_type,
            "location": self.location,
            "status": self.status,
            "images": self.images,
            "videos": self.videos,
            "comment": self.comment,
            "incidentId": self.public_incident_id
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

    def add_comment(self, comment_id, new_comment):
        for comment_to_update in self.incident_list:
             if comment_to_update.incident_id == comment_id:
                 comment_to_update.comment = new_comment
                 return "comment added"  
        return None
    
    def edit_red_flag(self, location_id, new_location):
        for location_to_update in self.incident_list:
             if location_to_update.incident_id == location_id and location_to_update.status == "draft":
                 location_to_update.location = new_location
                 return "location updated"  
        return None

    def update_status(self, status_id, new_status):
        for status_to_update in self.incident_list:
             if status_to_update.incident_id == status_id:
                 status_to_update.status = new_status
                 return "status updated"  
        return None

        
