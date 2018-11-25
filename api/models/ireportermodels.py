class User:

    def __init__(self, userId=int, firstName="", lastName="", 
                otherNames="", userName="", email="", password="", 
                registered="", isAdmin="False"):

        self.userId = userId
        self.firstName = firstName
        self.lastName = lastName
        self.otherNames = otherNames
        self.userName = userName
        self.email = email
        self.password = password
        self.registered = registered

users = []        
