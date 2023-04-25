#!/usr/bin/python3
"""
    script sends a request to a given URL and displays the response
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    result = requests.get(url)
    if result.status_code >= 400:
        print('Error code: {}'.format(result.status_code))
    else:
        print(result.text)
