#!/usr/bin/python3
"""script takes in a URL, sends request to it and displays the 
value of the variable in the response body
Usage: ./5-hbtn_header.py https://alx-intranet.hbtn.io
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    result = requests.get(url)
    print(result.headers.get("X-Request-Id"))
