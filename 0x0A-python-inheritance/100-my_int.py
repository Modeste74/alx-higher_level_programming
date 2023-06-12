#!/usr/bin/python3
"""defines a class
that inherits
"""


class MyInt(int):
    """represent MyInt"""
    def __eq__(self, other):
        """return inverse of '__ne__'"""
        return super().__ne__(other)

    def __ne__(self, other):
        """returns inverse of '__eq__'"""
        return super().__eq__(other)
