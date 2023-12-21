#!/usr/bin/python3
"""Class Module """


class Square:
    """A class of type square"""

    def __init__(self, size=0):
        """Creating the class constructor
        Args:
            size: Size of the square
        Raises:
            TypeError: If size is not of type int
            ValueError: When size is less than or equal to zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """Gets the size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        calculating the area of square
        Returns: The square of the size
        """

        return (self.__size ** 2)

    def my_print(self):
        """prints # """

        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)
