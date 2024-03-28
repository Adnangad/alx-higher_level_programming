#!/usr/bin/python3
"""Module displays request using request package"""
import requests

if __name__ == '__main__':
    rez = requests.get('https://alx-intranet.hbtn.io/status')
    rez = rez.text
    print("Body response:$")
    print(f'\t- type: {type(rez)}$')
    print(f'\t- content: {rez}$')
