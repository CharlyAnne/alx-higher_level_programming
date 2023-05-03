#!/usr/bin/python3
"""script takes in a URL and an email address, sends a POST request
to it with the email as the response"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    result = requests.post(url, data=value)
    print(result.text)
