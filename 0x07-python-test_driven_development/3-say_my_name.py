#!/usr/bin/python3
"""Define a function that
says the name of people
"""


def say_my_name(first_name, last_name=""):
    """Print a statement string
    followed by the name or names
    given as arguments
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {} ".format(first_name))
