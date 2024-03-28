#!/bin/bash
# displayys the methods available
echo "$(curl -s -i -X OPTIONS "$1" | grep -i "^allow:" | cut -d' ' -f2-)"
