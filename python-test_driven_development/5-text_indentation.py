#!/usr/bin/python3
"""
This module contains a function that printsa text with
2 new lines after each of these characters: ., ? and :.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in text:
        if char in ['.', '?', ':']:
            print(char)
            print()
        else:
            print(char, end='')
