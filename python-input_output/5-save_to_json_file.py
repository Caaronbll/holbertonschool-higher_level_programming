#!/usr/bin/python3
"""
Write a function that
writes an Object to a
text file, using a JSON
representation"""
import json


def save_to_json_file(my_obj, filename):
    """writes Object to file using JSON"""
    with open(filename.json, 'wb') as f:
        json.dump(filename, f)