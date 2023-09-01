#!/usr/bin/python3
"""takes a URL and email and makes a post request
to the URL with email as parameter and display"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    r = requests.post(url, data={"email": email})
    print(r.text)
