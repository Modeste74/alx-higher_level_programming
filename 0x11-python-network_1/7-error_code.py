#!/usr/bin/python3
"""sends a request and displays the body
of response and if error in status display
that also"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    if r.status_code == 200:
        print(r.text)
    elif r.status_code >= 400:
        print(f"Error code: {r.status_code}")
