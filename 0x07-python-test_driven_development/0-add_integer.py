#!/usr/bin/python3
"""
This module contains functions for basic arithmetic operations.
"""


def add_integer(a, b=98):
    """
    This function adds integers.
    Args:
    a (int or float): First number
    b (int or float): Second number (default 98 if not provided)

    Returns:
    int: The sum of a and b

    Raises:
    TypeError: If a or b is not an integer or float

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
