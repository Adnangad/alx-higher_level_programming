#!/usr/bin/python3
def uppercase(str):
    leng = len(str)
    for i in range(leng):
        if 'a' <= str[i] <= 'z':
            print("{}".format(chr(ord(str[i]) - 32)), end='')
        else:
            print("{}".format(str[i]), end='')

