#!/usr/bin/bash
#Bash script that takes in a URL and displays all HTTP methods
#!/bin/bash

# Check if the URL argument is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send an OPTIONS request to the server and extract the allowed methods
allowed_methods=$(curl -s -X OPTIONS -I "$1" | grep "Allow:" | tr -d '\r' | awk '{print $2}')

# Check if any methods were found
if [ -z "$allowed_methods" ]; then
  echo "No allowed methods found for $1"
else
  echo "Allowed HTTP methods for $1:"
  echo "$allowed_methods"
fi
