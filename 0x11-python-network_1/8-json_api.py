#!/usr/bin/python3
"""Module  sends a POST request url wuth a letter as a parameter"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) < 2:
        val = ""
    else:
        val = argv[1]
    payload = {'q': val}
    url = "http://0.0.0.0:5000/search_user"
    rez = requests.post(url, data=payload)
    try:
        fin = rez.json()
        if bool(fin) is False:
            print("No result")
        else:
            print("[{}] {}".format(fin['id'], fin['name']))
    except:
        print("Not a valid JSON")
