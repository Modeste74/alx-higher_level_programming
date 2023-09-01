#!/usr/bin/python3
"""takes github credentials and uses the
github api to display id"""
import sys
import requests


if __name__ == "__main__":
    usr_name = sys.argv[1]
    password = sys.argv[2]
    session = requests.Session()
    session.auth = (usr_name, password)
    url = 'https://api.github.com/user'
    r = session.get(url)
    r_data = r.json()
    print(r_data.get("id"))
