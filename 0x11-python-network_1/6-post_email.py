#!/usr/bin/python3
import requests
import sys
"""Module posts an email on an url"""


if __name__ == '__main__':
    data = {'email' : f'{sys.argv[2]}'}
    requests.post(f'{sys.argv[1]}', data=data)
