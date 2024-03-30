#!/bin/bash
# displays body of response
echo -n "$(curl -s "$1" -L)"
