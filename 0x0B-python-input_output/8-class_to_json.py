#!/usr/bin/python3
"""
Contains the "class_to_json" function
"""


def class_to_json(obj):
    """returns the dictionary description
     for JSON serialization of an object
    """
    if not isinstance(obj, object):
        raise ValueError("must be an instance of class")
    json_dict = {}
    for attr in dir(obj):
        if attr.startswith("__"):
            continue:
        value = getattr(obj, attr)
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[attr] = value
    return json_dict
