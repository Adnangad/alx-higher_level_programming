#!/usr/bin/python3
"""Module contains a function that finds the peak of a list"""


def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    i, j = 0, len(list_of_integers) - 1

    while j > i:
        center = (j + i) // 2
        if list_of_integers[center + 1] > list_of_integers[center]:
            i = center + 1
        else:
            j = center
    return list_of_integers[i]
