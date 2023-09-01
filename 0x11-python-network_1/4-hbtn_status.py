#!/usr/bin/python3
"""fetches a url a displays response"""
import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    r = requests.get(url)
    if r.status_code == 200:
        print("Body response:")
        print("\t- type: {}".format(type(r.text)))
        print("\t- content: {}".format(r.text))
    else:
        print(f"Request error: {r.status_code}")
