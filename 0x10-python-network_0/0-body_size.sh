#!/bin/bash
# this bash script takes in a URL, sends a request to the URL and 
# displays size of the body response.

curl -sI $1 | grep "Content-Length:" | cut -d " " -f 2
