#!/bin/bash
# sends a request including variables
echo -n "$(curl -s -d "X-School-User-Id=98" "$1")"
