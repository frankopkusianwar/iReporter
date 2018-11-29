class User:

    def __init__(self, user_id=int, first_name="", last_name="", 
                other_names="", user_name="", email="", password="", 
                registered="", isAdmin="False"):

        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.other_names = other_names
        self.user_name = user_name
        self.email = email
        self.password = password

users = []

class Incident:
    def __init__(self, incident_id=int, created_by="", created_on="",
                latitude="", longitude="", images=[], status="", comment=""):
        self.incident_id = incident_id
        self.created_by = created_by
        self.created_on = created_on
        self.latitude = latitude
        self.longitude = longitude
        self.images = images
        self.status = status
        self.comment = comment

class  RedFlag(Incident):
    """docstring for  RedFlag"""
    def __init__(self):
        Incident.__init__(self)
        self.red_flag_incident_type = "red-flag"

class  Intervention(Incident):
    """docstring for  RedFlag"""
    def __init__(self):
        Incident.__init__(self)
        self.internention_incident_type = "intervention"
        

incidents = []    
        
