#!/usr/bin/python3
"""This handles errors"""
import sys
import requests

if __name__ == '__main__':
    rez = requests.get(sys.argv[1])
    if rez.status_code >= 400:
        print(f"Error code: {rez.status_code}")
    else:
        print(rez.text)
