#!/bin/bash
# takes in a URL, sends a POST request to it and displays response
curl -sX POST -F "email=test@gmail.com" -F "subject=I will always be here for PLD" "$1"
