#!/usr/bin/python3
"""
This module open and appends files.
"""


def append_write(filename="", text=""):
    """
    This functions writes in files.

    Args:
    filename (str):the file to be opened.
    text (str):the trext to be appended.

    Return:
    none.
    """
    with open(filename, "a", encoding="utf8") as f:
        b = f.write(text)
        return b
