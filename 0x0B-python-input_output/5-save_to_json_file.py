#!/usr/bin/python3
"""
This module handles JSON.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    This func serealizes the object and writes it to a file.

    Args:
    my_obj:the object to be serialized and written.
    filename:the file to be written to.

    Return:
    None
    """
    with open(filename, "w", encoding="utf8") as f:
        json.dump(my_obj, f)
