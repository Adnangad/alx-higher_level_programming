#!/usr/bin/python3
"""Module posts"""
import urllib.parse
import urllib.request

if __name__ == '__main__':
    url = sys.argv[1]
    val = sys.argv[2]
    dat = {'email': val}
    data = urllib.parse.urlencode(dat)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        rez = response.read()
    print('Your email is ', val)
    print(rez.decode('utf-8'))
