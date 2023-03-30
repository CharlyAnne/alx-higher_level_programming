#!/bin/bash
# takes in a URL, sends a request to the URL and displays size of the body response.
curl -sI "$1" | grep -i "Content-length" | cut -d ":" -f 2
