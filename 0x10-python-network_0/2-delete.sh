#!/bin/bash
# sends a delete request
echo "$(curl -X DELETE -s "$1")"
