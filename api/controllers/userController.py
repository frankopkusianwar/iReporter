from flask import request, jsonify
from api.models.models import User, IreporterDb
from api.utilities import make_id, check_user, check_email, check_paswd
import uuid
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

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
        public_user_id = str(uuid.uuid4())

        validate_user = [first_name, last_name, other_names, username,email,password]
        if check_user(validate_user) == "invalid":
            return jsonify({
                "status": 400,
                "message": "please fill all fields"
            }),400

        if check_email(email) == "invalid":
            return jsonify({
                "status": 400,
                "message": "invalid email adress"
            }),400
        
        if check_paswd(password) == "invalid":
            return jsonify({
                "status": 400,
                "message": "password should be more than 8 characters"
            }),400
        
        hashed_password = generate_password_hash(user_data.get('password'), method='sha256')
        user = User(other_names, username, hashed_password, registered,
        user_id, first_name, last_name, email, is_admin, public_user_id)
        
        new_user.add_user(user)

        return jsonify({
            "data": [{
            "id": user_id,
            "status": 201,
            "message": "user created successfully", 
            }]
        }), 201
