#!/usr/bin/python3
"""Class Square that defines a square by: (based on 2-square.py)"""


class Square:
    """A class that represents a square"""

    def __init__(self, size=0):

        """Initializing a class called 'Square'
        Args:
            size: parameter represents size of the square
        Raises:
            TypeError: if the size is not an integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns: The square of the size"""

        return self.__size ** 2
