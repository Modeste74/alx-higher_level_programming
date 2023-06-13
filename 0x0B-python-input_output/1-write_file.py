#!/usr/bin/python3
"""define a function
that writes into a file
"""


def write_file(filename="", text=""):
    """writes into a file
    and returns count
    """
    with open(filename, "w", encoding="utf-8")as f:
        return f.write(text)
