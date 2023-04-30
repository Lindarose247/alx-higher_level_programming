#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URLand displays the value of the X-Request-Id variablefoundin the header of the response.
"""

import urllib.request
import sys

if __name__== "__main__":
    with urllib.request.urlopen(sys.argv[1]) as url:
        s =url.getheader('X-Request-Id')
        print("{}".format(s))
