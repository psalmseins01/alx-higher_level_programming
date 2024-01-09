#!/usr/bin/python3
"""Module  that defines a class MyInt which inherits from int class"""


class MyInt(int):
    """Class that inverts int operators == and !="""

    def __eq__(self, val):
        """Override '==' opeartor with '!='"""
        return self.real != val

    def __ne__(self, val):
        """Override '!=' operator with '==' """
        return self.real == val
