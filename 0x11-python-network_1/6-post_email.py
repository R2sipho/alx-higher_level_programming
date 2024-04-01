#!/usr/bin/python3
"""Sends a POST request with an email parameter and displays the response body."""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}
    r = requests.post(url, data=payload)

    print("Your email is: {}".format(email))
    print(r.text)
