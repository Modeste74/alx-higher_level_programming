#!/usr/bin/python3
"""defines a function that returns
true or false
"""


def is_same_class(obj, a_class):
    """return True or False
    depending on whether the obeject
    is an instance of that class
    """
    return type(obj) is a_class
