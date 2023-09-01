#!/usr/bin/python3
"""sends request and displays the value
of the response header X-Request-Id"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    header_name = 'X-Request-Id'
    r = requests.get(url)
    print(r.headers.get(header_name))
