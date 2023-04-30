#!/bin/bash
#a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the respons

curl -sI "$1" | grep 'Content-Length:' | cut -c 17-
