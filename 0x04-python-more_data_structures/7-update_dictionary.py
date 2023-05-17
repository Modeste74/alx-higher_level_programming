#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for n in a_dictionary:
        if n == key:
            a_dictionary[key] = value
    a_dictionary[key] = value
    return a_dictionary
