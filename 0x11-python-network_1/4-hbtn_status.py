#!/usr/bin/python3
"""This module fetches data from a URL using the requests package."""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    final = response.content

    print("Body response:")
    print(f'\t- type: {type(final)}')
    print(f'\t- content: {final}')
    print(f'\t- utf8 content: {final.decode("utf-8")}')
