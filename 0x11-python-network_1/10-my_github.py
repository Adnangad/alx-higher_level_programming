#!/usr/bin/python3
"""Gets user id of github"""
import sys
import requests


def get_id(usr_name, passwd):
    url = f"https://api.github.com/user"
    response = requests.get(url, auth=HTTPBasicAuth(usr_name, passwd))
    try:
        rez = response.json()
        return rez['id']
    except:
        return None
if __name__ == "__main__":
    usr_name = sys.argv[1]
    passwd = sys.argv[2]
    answer = get_id(usr_name, passwd)
    print(f"{answer}")
