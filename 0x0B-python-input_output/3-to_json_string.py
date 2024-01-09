#!/usr/bin/python3
"""
This module handles JSON.
"""

import json


def to_json_string(my_obj):
    """
    This func serealizes the object.

    Args:
    my_obj:the object to be serialized

    Return:
    The sterilized obj.
    """
    b = json.dumps(my_obj)
    return b
