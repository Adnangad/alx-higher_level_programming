#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 'a' <= str <= 'z':
            print("{}".format(chr(ord(str) - 32)), end='')
        else:
            print("{}".format(str), end='')
