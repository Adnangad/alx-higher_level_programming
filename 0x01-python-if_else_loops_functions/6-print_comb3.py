#!/usr/bin/python3
for i in range(9):
    for x in range(10):
        if i == x or (str(x) == "0") or (str(i) + str(x) > str(x) + str(i)):
            continue
        if (str(i) + str(x) != "89"):
            print("{}, ".format(str(i) + str(x)), end='')
        else:
            print("{}".format(str(i) + str(x)))
