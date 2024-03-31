#!/usr/bin/python3
import requests
import sys
"""Module posts an email on an url"""


if __name__ == '__main__':
    data = {'email' : sys.argv[2]}
    rez = requests.post(sys.argv[1], data=data)
    print(rez.text)
