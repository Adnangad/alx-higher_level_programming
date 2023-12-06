#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    rez = []
    for i in matrix:
        new = []
        for j in i:
            sq = j ** 2
            new.append(sq)
        rez.append(new)
    return rez
