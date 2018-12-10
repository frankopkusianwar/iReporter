import re
def make_id(chk, list_of_Items):
    new_id = 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    for obj in list_of_Items:
        if list_of_Items[-1] and chk == "userObject":
            new_id = obj.user_id + 1
        else:
            new_id = obj.incident_id + 1
    return new_id

def check_inc(fields,loc,img,vid):
    for field in fields:
        if not field:
            return "invalid"
        if type(loc) != dict or type(img) != list or type(vid) != list:
                return "invalid"
    return "valid"
    
def check_user(fields):
    for field in fields:
        if not field or type(field) != str or field.isspace():
            return "invalid"
    return "valid"

def check_email(mail):
    if not re.match(r"[^@.]+@[A-Za-z]+\.[a-z]+", mail):
        return "invalid"
    return "valid"

def check_paswd(passw):
    if len(passw) < 8:
        return "invalid"
    return "valid"