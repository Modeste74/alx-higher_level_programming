#!/usr/bin/python3
"""list 10 commit when the repo name
and username are passed"""
import sys
import requests


if __name__ == "__main__":
    repo = sys.argv[1]
    user = sys.argv[2]
    url = f'https://api.github.com/repos/{user}/{repo}/commits'
    r = requests.get(url)
    c_data = r.json()
    for commit in c_data[:10]:
        sha = commit.get("sha")
        author_name = commit.get("commit").get("author").get("name")
        print(f"{sha}: {author_name}")
