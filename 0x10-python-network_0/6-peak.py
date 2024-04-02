#!/usr/bin/python3
""" Locates a peak within an unsorted list of integers.
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list of integers to find peak of
    Returns: peak of list_of_integers or None
    """
    size = len(list_of_integers)
    mid_elem = size
    middle = size // 2

    if size == 0:
        return None

    while True:
        mid_elem = mid_elem // 2
        if (middle < size - 1 and
                list_of_integers[middle] < list_of_integers[middle + 1]):
            if mid_elem // 2 == 0:
                mid_elem = 2
            middle = middle + mid_elem // 2
        elif mid_elem > 0 and list_of_integers[middle] < list_of_integers[middle - 1]:
            if mid_elem // 2 == 0:
                mid_elem = 2
            middle = middle - mid_elem // 2
        else:
            return list_of_integers[middle]
