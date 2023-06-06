#!/usr/bin/python3
"""Defines a function print_square"""


def print_square(size):
    """print a square when
    given an int as an
    args
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
