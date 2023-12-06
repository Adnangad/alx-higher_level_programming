#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for x in matrix:
        for y in x:
            return (x**2, y**2)
