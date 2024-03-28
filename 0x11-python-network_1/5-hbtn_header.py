#!/usr/bin/python3
"""gets the value of a header"""
import requests
import sys

if __name__ == '__main__':
    rez = requests.get(sys.argv[1])
    di = rez.requests.header.get('X-Request-Id')
    print(di)
