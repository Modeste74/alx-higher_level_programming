#!/usr/bin/python3
"""define a class BaseGeometry"""


class BaseGeometry:
    """intializes the class"""
    def area(self):
        """raises Exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        if isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
