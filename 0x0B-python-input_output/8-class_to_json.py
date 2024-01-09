#!/usr/bin/python3
"""
This module deals with  JSON.
"""


def class_to_json(obj):
    """
    Returns dict description for JSON.

    Args:
    obj:the instance of class.

    Return:
    the dict description.
    """
    b = vars(obj)
    st = {}
    for a, c in b.items():
        if isinstance(c, (int, list, dict, str, bool)):
            st[a] = c
    return st
