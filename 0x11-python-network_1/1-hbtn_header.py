#!/usr/bin/python3
"""Retrieves values from a header"""
import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    with urllib.request.urlopen(url) as res:
        rez = res.getheader('X-Request-Id')
    print(rez)
