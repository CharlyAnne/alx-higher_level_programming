#!/usr/bin/python3
"""
    script takes two arguments that list 10 commits of a repository
    by a user, using a github API
    Usage: ./100-github_commits.py rails rails
"""
import requests
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
            sys.argv[2], sys.argv[1])

    req = requests.get(url)
    commits = req.json()
    try: 
        for i in range(10):
            print('{}: {}'.format(
                commits[i].get('sha'),
                commits[i].get('commit').get('author').get('name')))
    except IndexError:
        pass
