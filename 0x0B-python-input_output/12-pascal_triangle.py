#!/usr/bin/python3
"""
This module contains Pascal.
"""


def pascal_triangle(n):
    """
    This func is for pascals triangle.
    
    Args:
    n:the number of lists.

    Return:
    t.
    """
    if n <= 0:
        return []
    t = []
    for i in range(n):
        r = [1] * (i + 1)
        if i >= 2:
            for j in range(1, i):
                r[j] = t[i-1][j-1] + t[i-1][j]
        t.append(r)
    return t
