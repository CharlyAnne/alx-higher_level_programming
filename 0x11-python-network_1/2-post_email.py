#!/usr/bin/python3
"""script takes in a URL and an email, sends a POST request to the passed URL
    with the email as a parameter, to display the response body.
Usage: ./2-post_email.py <URL> <email>
"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(email)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        byte = response.read()
        print(byte.decode())
