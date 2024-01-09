#!/usr/bin/python3
"""
This module handles JSON.
"""

import json


def load_from_json_file(filename):
    """
    This func deserealizes the object and reads it.

    Args:
    filename:the file to be read.

    Return:
    None
    """
    with open(filename, "r", encoding="utf8") as f:
        json.load(f)
