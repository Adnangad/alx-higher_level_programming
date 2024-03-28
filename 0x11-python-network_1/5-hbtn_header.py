#!/usr/bin/python3
"""gets the value of a header"""
import requests
import sys

if __name__ == '__main__':
    rez = requests.header(sys.argv[1])
    print(rez.text)
