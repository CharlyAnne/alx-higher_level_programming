#!/usr/bin/python3
"""scriptstakes in a letter and sends a post request to url
with a given letter as a parameter
"""
import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) < 2:
        q = {'q': ""}
    else:
        q = {'q': sys.argv[1]}
    result = requests.post(url, data=q)
    try:
        response = result.json()
        if not response:
            print('No result')
        else:
            print(f"[{response.get('id')}] {response.get('name')}")
    except ValueError:
        print('Not a valid JSON')
