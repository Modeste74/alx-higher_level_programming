#!/usr/bin/python3
"""define a function
add_attribute
"""
def add_attribute(obj, attr, value):
    """adds a new attribute"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
