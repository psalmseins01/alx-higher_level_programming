#!/bin/bash
# Send request to URL, display only response status code
curl -s -o /dev/null -w "%{http_code}" "$1"
