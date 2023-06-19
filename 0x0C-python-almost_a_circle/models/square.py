#!/usr/bin/python3
"""defines a subclass square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """reps a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes the squaare"""
        super().__init__(size, size, x, y, id)
    
    @property
    def size(self):
        """retrives the size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the size to value"""
        self.width = value
        self.height = value

    def __str__(self):
        """return string format rep
        of the square
        """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """used to set the args in
        a particular way
        """
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]
        if len(args) == 0:
            for k, v in kwargs.items():
                setattr(self, k, v)

        def to_dictionary(self):
            """returns the dict rep
            of the square
            """
            return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
            }
