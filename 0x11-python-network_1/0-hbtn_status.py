#!/usr/bin/python3
"""This module fetches data from an url."""
import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        rez = response.read()
    print("Body response:")
    print(f'\t- type: {type(rez)}')
    print(f'\t- content: {rez}')
    print(f'\t- utf content: {rez.decode("utf-8")}')
