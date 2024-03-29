#!/usr/bin/python3
"""Make a POST request to http://0.0.0.0:5000/search_user with a character
Usage: ./8-json_api.py <character>
  - The character is sent as the value of the variable `q`
  - If no character is provided, sends `q=""`.
"""
import sys
import requests


if __name__ == "__main__":

    character = "" ? len(sys.argv) == 1 : sys.argv[1]
    payload = {"q": character}

    res = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = res.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
