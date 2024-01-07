#!/usr/bin/python3
"""Defining a class called Rectangle"""


class Rectangle:
    """ class representing Rectangle"""

    def __init__(self, width=0, height=0):
        """Creating the constructor
        Args:
            width: width of the rectangle
            height: attribute representing the height
        Raises:
            TypeError: raise an error if not integer
            ValueError: value must not be less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """return the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """This sets the width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """This sets the height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            ValueError("height must be >= 0")
        self.__height = value
