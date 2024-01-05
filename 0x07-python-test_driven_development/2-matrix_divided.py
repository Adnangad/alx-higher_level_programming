#!/usr/bin/python3
"""
This is a matrix module.
"""


def matrix_divided(matrix, div):
    """
    This is a long explanation.

    Args:
    matrix (list):a list
    div (int):a div

    Return:
    new matrix.
    """
    if not isinstance(matrix, list) or not all(isinstance(i, list)for i in matrix) or not all(isinstance(i, (int, float)) for row in matrix for i in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    r = len(matrix[0])
    for i in matrix:
        if len(i) != r:
            raise TypeError("row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    b = []
    for i in matrix:
        c = []
        for j in i:
            rez = round(j / div, 2)
            c.append(rez)
        b.append(c)
    return b
