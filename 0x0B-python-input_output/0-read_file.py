#!/usr/bin/python3
"""
This module reads files.
"""


def read_file(filename=""):
    """
    This functions reads files.

    Args:
    filename (str):the file to be read.

    Return:
    none.
    """
    with open(filename, encoding="utf8") as f:
        b = f.readlines()
        for i in b:
            print(i, end="")
