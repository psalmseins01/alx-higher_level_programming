#!/bin/bash
#Bash script that takes in a URL and displays all HTTP methods
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi
allowed_methods=$(curl -s -X OPTIONS -I "$1" | grep "Allow:" | tr -d '\r' | awk '{print $2}')
if [ -z "$allowed_methods" ]; then
  echo "No allowed methods found for $1"
else
  echo "Allowed HTTP methods for $1:"
  echo "$allowed_methods"
fi
