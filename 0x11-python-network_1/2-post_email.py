#!/usr/bin/python3
"""
Sends a POST request to a given URL with a given
email as a parameter and displays the body
of the response (decoded in utf-8)
"""
import sys
from urllib import request, parse


if __name__ == "__main__":
    values = {'email': sys.argv[2]}
    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))
