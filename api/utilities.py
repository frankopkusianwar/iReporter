def check_for_empty_fields(*fields):
    """this function checks for an empty field"""
    for field in fields:
        if not field:
            return True
def check_for_space(*fields):
    """this function checks for space in input field"""
    for field in fields:
        if field.isspace():
            return True
def check_for_string_input(*fields):
    """this function checks if input is a string"""
    for field in fields:
        if type(field) != str:
            return True
