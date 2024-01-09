#!/usr/bin/python3
"""
This module open and writes in files.
"""


def write_file(filename="", text=""):
    """
    This functions writes in files.

    Args:
    filename (str):the file to be opened.
    text (str):the trext to be written.

    Return:
    none.
    """
    with open(filename, "w", encoding="utf8") as f:
        b = f.write(text)
        return b
