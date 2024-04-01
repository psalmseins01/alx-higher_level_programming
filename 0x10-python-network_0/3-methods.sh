#!/bin/bash
#Bash script that takes in a URL and displays all

curl -sI "$1" | grep "allow" | cut -d " " -f 2-
