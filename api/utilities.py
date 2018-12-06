def make_id(chk, list_of_Items):
    new_id = 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    for obj in list_of_Items:
        if list_of_Items[-1] and chk == "userObject":
            new_id = obj.user_id + 1
        else:
            new_id = obj.incident_id + 1
    return new_id