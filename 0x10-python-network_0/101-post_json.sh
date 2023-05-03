#!/bin/bash
# script sends a JSON POST request to a URL passed, and displays the response body
body=$(cat $2); curl -s --header "Content-Type: application/json" -X POST -d "$body" "$1"
