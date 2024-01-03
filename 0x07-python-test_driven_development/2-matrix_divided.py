#!/usr/bin/python3
def matrix_divided(matrix, div):
    for i in matrix:
        for j in i:
            rez = j / div
            print("{}, ".format(rez))
        print()
    print()
