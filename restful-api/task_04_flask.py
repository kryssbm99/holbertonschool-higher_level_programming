#!/usr/bin/python3
"""A simple Flask API with basic user operations"""

from flask import Flask, jsonify, request, abort

app = Flask(__name__)

users = {}

@app.route("/")
def home():
    """Returns a welcome message"""
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    """Returns a list of all usernames in JSON format"""
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    """Returns the status of the server"""
    return "OK"

@app.route("/users/<username>")
def users_specific(username):
    """Returns the data of a specific user if found, otherwise returns an error"""
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    output = users[username]
    output["username"] = username

    return jsonify(output)

@app.route("/add_user", methods=["POST"])
def add_user():
    """Adds a new user from the JSON data in the POST request"""
    if request.get_json() is None:
        abort(400, "Not a JSON")

    req_data = request.get_json()

    if "username" not in req_data:
        return jsonify({"error": "Username is required"}), 400

    users[req_data["username"]] = {
        "name": req_data["name"],
        "age": req_data["age"],
        "city": req_data["city"]
    }

    output = {
        "username": req_data["username"],
        "name": req_data["name"],
        "age": req_data["age"],
        "city": req_data["city"]
    }
    return jsonify({"message": "User added", "user": output}), 201


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
