#!/usr/bin/python3
"""Module displays request using request package"""
import requests

if __name__ == '__main__':
    rez = requests.get('https://alx-intranet.hbtn.io/status')
    final = rez.content
    print("Body response:$")
    print(f'\t- type: {type(final)}$')
    print(f'\t- content: {final.decode("utf-8")}$')
