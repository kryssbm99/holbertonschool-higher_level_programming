#!/usr/bin/python3
"""
Function to check if an object is an instance of
a class that inherited from the specified class
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that
    inherited (directly or indirectly) from a_class; otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
