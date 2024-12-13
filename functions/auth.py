from flask_jwt_extended import JWTManager,create_access_token, get_jwt,verify_jwt_in_request
from flask import jsonify, request
import datetime
from http import HTTPStatus



jwt = JWTManager()

users = {
    "admin": {
        "password": "admin",
        "role": "admin"
    },
    "user" : {
        "password": "user_pass",
        "role": "user"
    }
}

def initialition_jwt(app):
    jwt.init_app(app)

def login():

    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    if username not in users or users[username]['password'] != password:
        return jsonify ({
            "error": "Invalid credentials"
        }), HTTPStatus.UNAUTHORIZED
    

    access_token = create_access_token(identity=username, fresh=True, expires_delta=datetime.timedelta(minutes=5))
    return jsonify(
        access_token = access_token
    ), HTTPStatus.OK



def validation():
    try:
        verify_jwt_in_request()

        claims = get_jwt()
        user_role = claims.get("role", "users") 

        if user_role != "admin":
            return jsonify({
                "error": "Permission denied"
                }), HTTPStatus.FORBIDDEN
        return None
    
    except Exception:
        return jsonify({
            "error": "An unexpected error occurred",
            "message": "No valid token provided. Please log in to access this resource."
        }), HTTPStatus.UNAUTHORIZED



