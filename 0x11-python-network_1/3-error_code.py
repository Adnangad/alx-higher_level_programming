#!/usr/bin/python3
"""This handles errors"""
import sys
import urllib.request
import urllib.error

if __name__ == '__main__':
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            rez = response.read().decode('utf-8')
            print(rez)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
