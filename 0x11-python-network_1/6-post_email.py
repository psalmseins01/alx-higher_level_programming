#!/usr/bin/python3
"""Make a POST request to a given 'url' with a given email
   Usage: ./6-post_email.py <URL> <email>
"""
import sys
import requests


if __name__ == "__main__":

    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    res = requests.post(url, data=value)
    print(res.text)
