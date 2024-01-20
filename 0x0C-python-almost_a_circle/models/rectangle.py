#!/usr/bin/python3
"""
    class Rectangle which inherits Base functionality
"""
from models.base import Base


class Rectangle(Base):
    """
        class Rectangle implements Base class
        Methods:
            __init__(): class constructor
            width: width of the rectangle
            height: height of the rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Initializing the class instance
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
            Getter for __width
            Returns: the value of the width
        """
        return self.__width

    @width.setter
    def width(self, val):
        """
            Setter for the width.
            Args:
                val (int): integer value to be set
        """
        if type(val) != int:
            raise TypeError("'width' must be an integer")
        if val <= 0:
            raise ValueError("'width' must be > 0")

        self.__width = val

    @property
    def height(self):
        """
            Getter for the height of the rectangle
            Returns: height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, val):
        """
            Setter for the height attribute
            Args:
                val (int): value to be set by the setter
        """
        if type(val) != int:
            raise TypeError("'height' must be an integer")
        if val <= 0:
            raise ValueError("'height' must be > 0")

        self.__height = val

    @property
    def x(self):
        """
            Getter for x.
            Returns: x
        """
        return self.__x

    @x.setter
    def x(self, val):
        """
            Setter for x.
            Args:
                val (int): value to be set by the setter.
        """
        if type(val) != int:
            raise TypeError("'x' must be an integer")
        if val < 0:
            raise ValueError("'x' must be >= 0")

        self.__x = val

    @property
    def y(self):
        """
            Getter for y
            Returns: y
        """
        return self.__y

    @y.setter
    def y(self, val):
        """
            Setter for y
            Args:
                val (int): value to be set by the setter.
        """
        if type(val) != int:
            raise TypeError("'y' must be an integer")
        if val < 0:
            raise ValueError("'y' must be >= 0")

        self.__y = val

    def area(self):
        """
            This function returns the area of the Rectangle instance.
        """
        return (self.__width * self.__height)

    def display(self):
        """
           This function prints to stdout the Rectangle instance with '#'
        """
        rect = ""
        print_symbol = "#"

        print("\n" * self.y, end="")

        for i in range(self.height):
            rect += (" " * self.x) + (print_symbol * self.width) + "\n"
        print(rect, end="")

    def __str__(self):
        """
            This returns a str formart of the rectangle
        """
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                                                self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
            The function assigns key/value argument to attributes
            kwargs.

            Args:
                *args -  variable number of arguments
                **kwargs - key-word arguments
        """
        if len(args) == 0:
            for k, v in kwargs.items():
                self.__setattr__(k, v)
            return

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """
            returns the dictionary repr of a rect
        """
        return {'x': getattr(self, "x"), 'y': getattr(self, "y"),
                'id': getattr(self, "id"), 'height': getattr(self, "height"),
                'width': getattr(self, "width")}
