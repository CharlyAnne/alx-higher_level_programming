#!/usr/bin/python3
"""this script fetches https://alx-intranet.hbtn.io/status."""
import urllib.request

request = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(request) as response:
    the_body = response.read()

print('Body response:')
print('\t- type: {}'.format(type(the_body)))
print('\t- content: {}'.format(the_body))
print('\t- utf8 content: {}'.format(the_body.decode()))
