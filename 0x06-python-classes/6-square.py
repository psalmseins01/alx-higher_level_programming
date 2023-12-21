#!/usr/bin/python3
"""Square Module"""


class Square:
    """Square class creation"""

    def __init__(self, size=0, position=(0, 0)):
        """Setting up the constructor
        Args:
            size: length of each side
            position: coordinate
        """
        self.size = size
        self.position = position

    def __str__(self):
        self.my_print()

    @property
    def size(self):
        """"size method definition
        Raises:
            TypeError: if size is not an instance of int type
            ValueError: if size < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Coordinates of this Square
        Raises:
            TypeError: if value != a tuple of 2 integers < 0
        """
        return self.__position

    @position.setter
    def position(self, value):
        """set the position of this Square
        Args: tuple of two positive integers
        Raises:
            TypeError: if value is not a tuple
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Get the area of a Square
        Returns: The size
        """
        return self.__size * self.__size

    def pos_print(self):
        """returns the position in space"""
        positn = ""
        if self.size == 0:
            return "\n"
        for w in range(self.position[1]):
            positn += "\n"
        for w in range(self.size):
            for i in range(self.position[0]):
                positn += " "
            for j in range(self.size):
                positn += "#"
            positn += "\n"
        return positn

    def my_print(self):
        """print the square in position"""
        print(self.pos_print(), end='')
