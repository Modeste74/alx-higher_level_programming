#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for n in a_dictionary:
        new_dict[n] *= 2
    return new_dict
