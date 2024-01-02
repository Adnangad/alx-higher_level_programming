#!/usr/bin/python3
"""
This module prints strings.
"""

def say_my_name(first_name, last_name=""):
    """
    Prints two strings.

    Args:
    first_name (str): first name
    last_name (str): last name

    Returns:
    None
    """
    if not isinstance(first_name, str):
        raise TypeError("first name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last name must be a string")
    print("My name is {} {}".format(first_name, last_name))
