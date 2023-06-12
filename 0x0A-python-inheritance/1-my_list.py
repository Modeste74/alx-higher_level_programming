#!/usr/bin/python3
"""
defines a sublcass MyList
that inherits from the super
list
"""


class MyList(list):
    """a subclass that inherits
    from a super
    """
    def print_sorted(self):
        """prints a sorted list"""
        sorted_list = sorted(self)
        print(sorted_list)
