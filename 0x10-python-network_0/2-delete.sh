#!/bin/bash
# sends a delete request
echo -n "$(curl -X DELETE -s "$1")"
