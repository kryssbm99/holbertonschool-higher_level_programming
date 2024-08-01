#!/usr/bin/python3
"""
This module provides a function `class_to_json` to return the dictionary
description for JSON serialization of an object.
"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure (list,
    dictionary, string, integer, and boolean) for JSON serialization of an
    object."""
    return obj.__dict__
