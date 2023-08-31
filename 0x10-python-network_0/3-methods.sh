#!/bin/bash
# show all possible methods
curl -sL -X OPTIONS $1 | grep 'Allow:' | cut -d ' ' -f2-
