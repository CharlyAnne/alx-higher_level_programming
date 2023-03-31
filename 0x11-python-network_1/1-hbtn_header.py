#!/usr/bin/python3
"""this script takes in a URL, sends a request to it and displays the value
    of the X-Request-ID variable"""
import urllib.request
import sys

url = sys.argv[1]

request = urllib.request.Request(url)
with urllib.request.urlopen(request) as response:
    print(dict(response.headers).get('X-Request-Id'))
