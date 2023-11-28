#!/usr/bin/python3
for i in range(9):
    for x in range(10):
        if i == x or (str(i) + str(x) == "10"):
            continue
        if (str(i) + str(x) != "89"):
            print(str(i) + str(x) + ", ", end='')
        else:
            print(str(i) + str(x))
