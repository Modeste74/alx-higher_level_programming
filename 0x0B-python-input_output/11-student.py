#!/usr/bin/python3
"""define a class student"""


class Student:
    """reps a student"""
    def __init__(self, first_name, last_name, age):
        """initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary
        rep of student
        """
        if attrs is None:
            return self.__dict__
        else:
            json_dict = {}
            for i in attrs:
                if hasattr(self, i):
                    json_dict[i] = getattr(self, i)
            return json_dict

    def reload_from_json(self, json):
        """replaces all attributes
        of the Student instance
        """
        for i, value in json.items():
            setattr(self, i, value)
