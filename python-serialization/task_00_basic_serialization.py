#!/usr/bin/python3
"""Creates basic serialization module"""
import json


def serialize_and_save_to_file(data, filename):
    """Serializes a dictionary and saves it to a file"""
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)


def load_and_deserialize(filename):
    """Loads JSON data from a file and deserializes it into a dictionary"""
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data
