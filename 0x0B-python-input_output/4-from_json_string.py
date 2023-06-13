#!/usr/bin/python3
"""importing of json and makes use of it"""

import json


def from_json_string(my_str):
    """return a deserialzed JSON data"""
    return json.loads(my_str)
