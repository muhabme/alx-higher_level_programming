#!/usr/bin/python3
"""
A script that takes in a URL, sends a
request to the URL and displays the value
of the `X-Request-Id` variable found in
the header of the response.
"""
import requests
from sys import argv

if __name__ == "__main__":
    data = {"email": argv[2]}
    r = requests.post(argv[1], data=data)
    print(r.text)
