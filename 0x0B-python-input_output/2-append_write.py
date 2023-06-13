#!/usr/bin/python3
"""define a function that
appends text to a file
"""


def append_write(filename="", text=""):
    """appends text to file
    and returns count of
    appended text
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
