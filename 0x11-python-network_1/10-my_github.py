#!/usr/bin/python3
"""scripts uses the github API to display a ID with given credentials.
Usage: ./10-my_github.py <github username> <github password>
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    cred = HTTPBasicAuth(username=sys.argv[1], password=sys.argv[2])
    resq = requests.get('https://api.github.com/user', auth=cred)
    print(resq.json().get('id'))
