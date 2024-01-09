#!/usr/bin/python3
"""A Module that inherits from the "/list class"/ """


class MyList(list):
    """Class that inherits from list"""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
