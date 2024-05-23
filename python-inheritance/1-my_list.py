#!/usr/bin/python3
"""
Class MyList that inherits from list and
includes a method to print the list sorted
"""


class MyList(list):
    """
    A subclass of list with a method to print the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        print(sorted(self))
