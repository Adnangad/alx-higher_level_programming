#!/bin/bash
# sends a delete request
echo "$(curl -s -X DELETE "$1")"
