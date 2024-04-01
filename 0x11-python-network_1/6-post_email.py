#!/usr/bin/python3
"""
Sends a post request with email as a parameter
"""
import requests
from sys import argv


if __name__ =="__main__":
    pas = {'email': argv[2]}
    url = argv[1]
    rez = requests.post(url, data=pas)
    print(rez.text)
