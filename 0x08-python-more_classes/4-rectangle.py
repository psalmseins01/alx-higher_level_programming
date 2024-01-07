#!/usr/bin/python3
"""defining a rectangle class"""


class Rectangle:
    """creating a rectangle class"""

    def __init__(self, width=0, height=0):
        """constructor for the rectangle class
        Args:
            width: attribute that represents the width of the rectangle
            height: attribute that represents the height of the rectangle
        Raises:
            TypeError: where 'size' is not integer
            ValueError: where 'size' is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the  width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self) -> str:
        """presents a diagram of the rectangle defined for an object"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for col in range(self.__height):
            for row in range(self.__width):
                rectangle += "#"
            if col < self.__height - 1:
                rectangle += "\n"
        return (rectangle)

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
