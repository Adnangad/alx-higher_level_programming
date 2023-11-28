#!/usr/bin/python3
def pow(a, b):
    result = 1
    if b < 0:
        return 1 / pow(a, -b)
    for i in range(b):
        result *= a
    return result
