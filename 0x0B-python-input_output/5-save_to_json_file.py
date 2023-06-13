#!/usr/bin/python3
"""makes use of json"""
import json


def save_to_json_file(my_obj, filename):
    """write to a file using JSON rep"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
