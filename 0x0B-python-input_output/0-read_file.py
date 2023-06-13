#!/usr/bin/python3
"""define a function that
reads a file
"""


def read_file(filename=""):
    """opens a file, reads it
    and the prints to stdout
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
