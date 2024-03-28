#!/usr/bin/python3
"""Make a POST request to a given 'URL' with a given 'email'
   Usage: ./2-post_email.py <url> <email>
  - Displays the body of the response.
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    val = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(val).encode("ascii")

    res = urllib.request.Request(url, data)
    with urllib.request.urlopen(res) as response:
        print(response.read().decode("utf-8"))
