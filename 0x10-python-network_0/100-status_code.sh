#!/bin/bash
# it sends req to an URL and displays the status code of the resp
echo -n "$(curl -o /dev/null -sw "%{http_code}" "$1")"
