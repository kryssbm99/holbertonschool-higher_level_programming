#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers.
    This function takes two arguments, 'a' and 'b',
    which must be either integers or floats.
    If the arguments are floats,
    they are cast to integers before performing the addition.
    If either argument is not an integer or a float, a TypeError is raised.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
