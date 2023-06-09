#!/usr/bin/python3
"""Defines a class Base"""
import json
import csv
import turtle


class Base:
    """represents a base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the json string
        rep of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        if len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string rep
        of all list_objs to a file
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        dict_list = [obj.to_dictionary() for obj in list_objs]
        json_rep = cls.to_json_string(dict_list)
        with open(filename, "w") as f:
            f.write(json_rep)

    @staticmethod
    def from_json_string(json_string):
        """return a dict list of json
        rep in json_string
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """return an instance where
        all attributes are set
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            dummy_instance = cls()
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """return list instances
        from json cls files
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                data_read = f.read()
                list_read = cls.from_json_string(data_read)
                inst_list = [cls.create(**data) for data in list_read]
                return inst_list
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as f:
            writer = csv.writer(f)
            if cls.__name__ == "Rectangle":
                fields = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                fields = ["id", "size", "x", "y"]
            writer.writerow(fields)
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """deserializes from csv"""
        filename = cls.__name__ + ".csv"
        instances = []
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                instance = cls.create(**row)
                instances.append(instance)
        return instances

    @staticmethod
    def draw(list_rectangle, list_square):
        """opens window and draws all
        rectangle and squares
        """
        window = turtle.Screen()
        window.setup(width=800, height=600)
        window.title("Rectangles and Squares")
        rectangle_turtle = turtle.Turtle()
        rectangle_turtle.shape("turtle")
        rectangle_turtle.pensize(3)
        rectangle_turtle.color("#ffffff")
        rectangle_turtle.screen.bgcolor("#b7312c")
        square_turtle = turtle.Turtle()
        square_turtle.shape("turtle")
        square_turtle.color("#ffffff")
        square_turtle.pensize(3)
        square_turtle.screen.bgcolor("#b7312c")
        for rect in list_rectangle:
            rectangle_turtle.penup()
            rectangle_turtle.goto(rectangle.x, rectangle.y)
            rectangle_turtle.pendown()
            for i in range(2):
                rectangle_turtle.forward(rectangle.width)
                rectangle_turtle.left(90)
                rectangle_turtle.forward(rectangle.height)
                rectangle_turtle.left(90)
        for sqr in list_rectangle:
            square_turtle.penup()
            square_turtle.goto(square.x, square.y)
            square_turtle.pendown()
            for i in range(4):
                square_turtle.forward(square.size)
                square_turtle.left(90)
        window.exitonclick()
