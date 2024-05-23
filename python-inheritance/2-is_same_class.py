#!/usr/bin/python3
"""
Function to check if an object is exactly an instance of a specified class
"""


def is_same_class(obj, a_class):
    """
    Returns True if obj is exactly an instance of a_class; otherwise False.

    obj: The object to check.
    a_class: The class to compare against.

    True if obj is an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
