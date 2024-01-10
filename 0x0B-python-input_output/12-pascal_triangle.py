#!/usr/bin/python3
"""
This module contains Pascal.
"""


def pascal_triangle(n):
    t = []
    for i in range(n):
        r = [1] * (i + 1)
        if i >= 2:
            for j in range(1, i):
                r[j] = t[i-1][j-1] + t[i-1][j]
        t.append(r)
    return t
