#!/usr/bin/python3
"""define a function that
returns True or False
"""


def inherits_from(obj, a_class):
    """checks and return True or false
    if the object is an instance of a class
    that inherited from the specified class
    directly or otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
