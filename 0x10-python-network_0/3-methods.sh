#!/bin/bash
# displayys the methods available
echo "$(curl -X OPTIONS -s "$1")"
