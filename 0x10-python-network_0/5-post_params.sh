#!/bin/bash
# Send POST request via curl to given URL, show response body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
