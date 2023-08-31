#!/usr/bin/python3
"""defines a function find_peak"""


def find_peak(list_of_integers):
    """function that return the peak"""
    if not list_of_integers:
        return None
    num = list_of_integers
    length = len(num) - 1
    peak = 0
    for n in range(1, length):
        if num[n] >= num[n + 1] and num[n] >= num[n - 1]:
            peak = num[n]
    if len(set(num)) == 1:
        peak = num[0]
    if num[0] > peak:
        peak = num[0]
    if num[length] > peak:
        peak = num[length]
    return peak
