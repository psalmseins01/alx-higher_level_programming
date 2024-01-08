#!/usr/bin/python3
"""

Module comprised a function that multiplies 2 matrices

"""


def matrix_mul(m_a, m_b):
    """ multiplies 2 matrices

    Args:
        m_a: matrix a
        m_b: matrix b

    Returns:
        return result

    Raises:
        TypeError: if m_a or m_b aren't a list
        TypeError: if m_a or m_b aren't a list of a lists
        ValueError: if m_a or m_b are empty
        TypeError: if the lists of m_a or m_b don't have integers or floats
        TypeError: if the rows of m_a or m_b don't have the same size
        ValueError: if m_a and m_b can't be multiplied


    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for elems in m_a:
        if not isinstance(elems, list):
            raise TypeError("m_a must be a list of lists")

    for elems in m_b:
        if not isinstance(elems, list):
            raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    for lists in m_a:
        for elems in lists:
            if not type(elems) in (int, float):
                raise TypeError("m_a should contain only integers or floats")

    for lists in m_b:
        for elems in lists:
            if not type(elems) in (int, float):
                raise TypeError("m_b should contain only integers or floats")

    lent = 0

    for elems in m_a:
        if lent != 0 and lent != len(elems):
            raise TypeError("each row of m_a must be of the same size")
        lent = len(elems)

    lent = 0

    for elems in m_b:
        if lent != 0 and lent != len(elems):
            raise TypeError("each row of m_b must be of the same size")
        lent = len(elems)

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    r1 = []
    j1 = 0

    for a in m_a:
        r2 = []
        j2 = 0
        num = 0
        while (j2 < len(m_b[0])):
            num += a[j1] * m_b[j1][j2]
            if j1 == len(m_b) - 1:
                j1 = 0
                j2 += 1
                r2.append(num)
                num = 0
            else:
                j1 += 1
        r1.append(r2)

    return r1
