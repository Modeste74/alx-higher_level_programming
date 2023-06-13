#!/usr/bin/python3
"""defines function append_after"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text
    inside a file after
    search_string
    """
    with open(filename, "r+", encoding="utf-8") as f:
        line = f.readlines()
        f.seek(0)
        for i in line:
            f.write(i)
            if search_string in i:
                f.write(new_string)
        f.truncate()
