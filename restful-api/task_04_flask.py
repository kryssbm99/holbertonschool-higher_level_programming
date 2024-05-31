#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(list(users.keys()))

@app.route('/status', methods=['GET'])
def get_status():
    return "OK"

@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    user_data = request.json
    username = user_data.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data})

if __name__ == "__main__":
    app.run(debug=True)
