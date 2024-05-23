#!/usr/bin/python3
"""
Module that defines a function to return the list
of available attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods
    of an object.

    A list of strings representing the names of the
    attributes and methods of the object.
    """

    hello_obj = dir(obj)
    return dir(obj)
