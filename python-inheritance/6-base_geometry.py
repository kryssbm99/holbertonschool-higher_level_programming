#!/usr/bin/python3
"""
Class BaseGeometry with a method area that raises an Exception
"""


class BaseGeometry:
    """
    A class named BaseGeometry.
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")
