class User:
    """model class for user"""
    def __init__(self,args):
        self.user_id = args['userId']
        self.first_name = args['firstName']
        self.last_name = args['lastName']
        self.other_names = args['otherNames']
        self.user_name = args['userName']
        self.email = args['email']
        self.password = args['password']
        self.registered = args['registered']
        self.isAdmin = False

users = []

class Incident:
    """model class for incident"""
    def __init__(self, args):
        self.incident_id = args['incident_id']
        self.created_by = args['created_by']
        self.created_on = args['created_on']
        self.latitude = args['latitude']
        self.longitude = args['longitude']
        self.images = args['images']
        self.status = args['status']
        self.comment = args['comment']

class  RedFlag(Incident):
    """model class for  RedFlags"""
    def __init__(self, red_flag_incident_type):
        super.__init__(self,)
        self.red_flag_incident_type = red_flag_incident_type

class  Intervention(Incident):
    """model class for interventions"""
    def __init__(self, internention_incident_type):
        super.__init__(self)
        self.internention_incident_type = internention_incident_type
        

incidents = []    
        
