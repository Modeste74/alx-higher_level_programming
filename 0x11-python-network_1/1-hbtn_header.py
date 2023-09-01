#!/usr/bin/python3
"""displays the value of the
X-Request-Id
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        header_name = "X-Request-Id"
        header_content = response.headers.get(header_name)
        if header_content is None:
            print("Nothing present")
        else:
            print(header_content)
