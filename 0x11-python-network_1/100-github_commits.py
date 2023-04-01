#!/usr/bin/python3
"""
    takes 2 args that list 10 commits of a given repo, using github API
    Usage: ./100-github_commits.py rails rails
"""
import requests
import sys

if __name__ == "__main__":
    url = f'https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits'

    req = requests.get(url)
    commits = req.json()
    try: 
        for i in range(10):
            print('{}: {}'.format(
                commits[i].get('sha'),
                commits[i].get('commit').get('author').get('name')))
    except IndexError:
        pass
