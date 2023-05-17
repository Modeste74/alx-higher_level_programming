#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_key = None
    max_value = float('-inf')
    for n, m in a_dictionary.items():
        if m > max_value:
            max_key = n
            max_value = m
    return max_key
