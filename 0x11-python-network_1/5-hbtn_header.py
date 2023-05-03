#!/usr/bin/python3
"""script sends request to a given URL and displays the X-Request-Id
    as response body
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    result = requests.get(url)
    print(result.headers.get("X-Request-Id"))
