#!/usr/bin/python3
"""Module sends a post request"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    pas = {'email': argv[2]}
    data = urllib.parse.urlencode(pas)
    data = data.encode('utf8')
    url = argv[1]
    rez = urllib.request.Request(url, data)
    with urllib.request.urlopen(rez) as response:
        fin = response.read()
        print(fin.decode('utf8'))
