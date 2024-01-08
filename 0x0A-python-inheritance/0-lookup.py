#!/usr/bin/python3
"""
This module looks up an objct.
"""


def lookup(obj):
    """
    It llooks up a list.

    Args:
    obj (class):The class to be looked at.

    Return:list object.
    """
    ls = list(obj.__dict__)
    return ls
