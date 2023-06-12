#!/usr/bin/python3
"""defines a function that
returns True or False
if the instance of an obj is
that of a class inherited from
a specific class
"""


def is_kind_of_class(obj, a_class):
    """checks if an is an instance
    of a class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
