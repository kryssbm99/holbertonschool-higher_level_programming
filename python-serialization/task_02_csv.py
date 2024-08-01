#!/usr/bin/python3
"""Reads data in CSV format and converts it to JSON format."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Converts a CSV file to a JSON file."""
    try:
        with open(csv_filename, mode='r') as csv_f:
            csv_reader = csv.DictReader(csv_f)
            data = [row for row in csv_reader]

        with open('data.json', mode='w') as json_f:
            json.dump(data, json_f, indent=4)

        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
