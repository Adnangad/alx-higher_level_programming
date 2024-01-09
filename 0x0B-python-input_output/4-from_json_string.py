#!/usr/bin/python3
"""
This module handles JSON.
"""

import json


def from_json_string(my_str):
    """
    This func deserealizes the str.

    Args:
    my_str:the str to be deserialized

    Return:
    The desterilized str.
    """
    b = json.loads(my_str)
    return b
