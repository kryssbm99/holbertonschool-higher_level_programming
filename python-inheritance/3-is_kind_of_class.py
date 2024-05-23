#!/usr/bin/python3
"""
Function to check if an object is an instance of, or if the object
is an instance of a class that inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of, or if the object is an
    instance of a class that inherited from, a_class; otherwise False.
    """
    return isinstance(obj, a_class)
