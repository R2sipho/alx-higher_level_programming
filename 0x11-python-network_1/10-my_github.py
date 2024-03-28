#!/usr/bin/python3
"""Displays the user id of a GitHub user."""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"
    try:
        r = requests.get(url, auth=(username, token))
        if r.status_code == 200:
            user_id = r.json()["id"]
            print(user_id)
        else:
            print("None")
    except Exception as e:
        print("None")

