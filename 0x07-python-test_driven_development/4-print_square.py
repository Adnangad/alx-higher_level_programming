#!/usr/bin/python3
"""
This module prints.
"""


def print_square(size):
    """
    Prints # according to size.

    Args:
    size (int):number of # to be printed

    Returns:
    none
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for k in range(size):
            print("#", end='')
        print()
