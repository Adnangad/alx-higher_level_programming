#!/usr/bin/python3
def uppercase(str):
    for i in str:
        up = i
        if 'a' <= i <= 'z':
            up = chr(ord(i) - 32)
        print("{}".format(up), end='')
    print()
