#!/usr/bin/python3
"""takes in a letter and posts it to
the url as a parameter and intern displays
[<id>] <name>"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""
    url = 'http://0.0.0.0:5000/search_user'
    data = {"q": q}
    try:
        r = requests.post(url, data=data)
        r_data = r.json()
        if r_data:
            user = r_data
            user_id = user.get("id")
            user_name = user.get("name")
            print(f"[{user_id}] {user_name}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
