#!/usr/bin/python3
"""imports sys and json
and two other function
to make the following
function work
"""
import sys
import json

sj = __import__("5-save_to_json_file").save_to_json_file
lj = __import__("6-load_from_json_file").load_from_json_file


def add_item_to(args, filename):
    """adds args to list and
    saves them in a file
    """
    try:
        existing_data = lj(filename)
    except FileNotFoundError:
        existing_data = []
    existing_data.extend(args)
    sj(existing_data, filename)
    with open(filename, "a") as f:
        f.write("\n")


add_item_to(sys.argv[1:], "add_item.json")
