#!/usr/bin/env python3

import sys

from mitmproxy import io
from mitmproxy.exceptions import FlowReadException

if len(sys.argv) != 2:
    print(f'Usage: {sys.argv[0]} filename.mitmproxy')
    sys.exit(1)
filename = sys.argv[1]

with open(filename, 'rb') as filehandle:
    # The FlowReader object reads the mitmproxy file
    freader = io.FlowReader(filehandle)
    try:
        for flow in freader.stream():
            # Each Flow contains a single transaction, for example a HTTP request and response.
            print(flow.request.url) # Print each request URL
            if "Referer" in flow.request.headers: # If the request contains a Referer-header, print it as well.
                print(f'\tReferer: {flow.request.headers["Referer"]}')
            # help(flow.request) # Show documentation for the flow.request object and it's methods
            # break # When using the help() function, exit the loop to prevent showing the documentation over and over again.
            # print(dir(flow.response)) # The dir() function simply lists an objects' method and attribute names
            # Online documentation about the flow object can be found on https://mitmproxy.readthedocs.io/en/v2.0.2/scripting/api.html#mitmproxy.http.HTTPFlow
    except FlowReadException as e:
        print(f'Flow file corrupted: {e}')
