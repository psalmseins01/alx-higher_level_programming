#!/usr/bin/python3
"""Module that defines BaseGeometry"""


class BaseGeometry:
    """BaseGeometry class defination"""

    def area(self):
        """Method that defines area"""
        raise Esception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates a value as an integer"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
