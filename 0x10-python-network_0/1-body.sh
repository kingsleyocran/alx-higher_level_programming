#!/bin/bash
# takes in a URL, sends a GET request to the URL,
# and displays the body of a 200 status code response
curl -s "$1" -X GET -L 
