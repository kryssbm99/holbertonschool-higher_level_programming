#!/usr/bin/python3
"""
A Flask application demonstrating basic and JWT authentication.
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

# Sample users data
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['JWT_SECRET_KEY'] = 'supersecretkey'
jwt = JWTManager(app)

@auth.verify_password
def verify_password(username, password):
    """
    Verifies the username and password for basic authentication.
    """
    user = users.get(username)
    if user and check_password_hash(user.get('password'), password):
        return username

@app.route('/basic-protected')
@auth.login_required
def basicprotected():
    """
    Endpoint protected by basic authentication.
    """
    return "Basic Auth: Access Granted"

@app.route('/login', methods=['POST'])
def login():
    """
    Login endpoint to authenticate user and return a JWT token.
    """
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username or not password:
        return jsonify({"msg": "Missing username or password"}), 400

    user = users.get(username)
    if user and check_password_hash(user.get('password'), password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Invalid username or password"}), 401

@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def protected():
    """
    Endpoint protected by JWT authentication.
    """
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

@app.route('/admin', methods=['GET'])
@jwt_required()
def admin_route():
    """
    Admin-specific endpoint protected by JWT authentication.
    """
    current_user = get_jwt_identity()
    user_role = users.get(current_user, {}).get('role', '')
    if user_role == 'admin':
        return jsonify(message=f"Hello admin {current_user}!"), 200
    else:
        return jsonify({"msg": "Unauthorized"}), 403
    
@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """
    Another admin-specific endpoint protected by JWT authentication.
    """
    current_user = get_jwt_identity()
    user_role = users.get(current_user, {}).get('role', '')
    if user_role == 'admin':
        return jsonify(message="Admin Access: Granted"), 200
    else:
        return jsonify({"msg": "Unauthorized"}), 403

if __name__ == '__main__':
    app.run(debug=True)
