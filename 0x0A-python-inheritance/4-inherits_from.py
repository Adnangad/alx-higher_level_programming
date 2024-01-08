#!/usr/bin/python3
"""
This module checks if an object is an instance of a class.
"""


def inherits_from(obj, a_class):
    """
    Checks if is instance.

    Args:
    obj (class):the object to be checked
    a_class (class):the measure

    Return:
    True if isinstance
    False if not.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
