#!/bin/bash
# Send JSON POST request to URL, display response body
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
