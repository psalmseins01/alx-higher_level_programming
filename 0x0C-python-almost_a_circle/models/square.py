#!/usr/bin/python3
"""
    This is a class Square that inherits Rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        creates Square class
        """
    def __init__(self, size, x=0, y=0, id=None):
        """
            Square class constructor (This overrides Rectangle init)
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
            Getter for the size of the square
        """
        return self.width

    @size.setter
    def size(self, val):
        """
            Setter for the value of size
        """
        if type(val) != int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")

        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """
            key-value argument to attributes
            kwargs is skipped if args is not empty
            Args:
                *args -  variable number of arguments
                **kwargs - keyworded arguments
        """
        if len(args) == 0:
            for k, v in kwargs.items():
                self.__setattr__(k, v)
            return

        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def __str__(self):
        """
            str function overloading
        """
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                             self.id, self.x, self.y,
                                             self.width)

    def to_dictionary(self):
        """
            Dictionary representation of a square
        """
        return {'id': getattr(self, "id"),
                'size': getattr(self, "width"),
                'x': getattr(self, "x"),
                'y': getattr(self, "y")}
