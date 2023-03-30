#!/bin/bash
# takes in a URL, sends a POST request to it and displays response
curl -s $1 -X POST -d "email=test@gmail.com&subject=I will always be there for PLD"
