#!/bin/bash
# displays body of response
{ res=$(curl -s -w "%{http_code}" "$1");stat=$(tail -n 1 <<< "$res"); [ "$stat" -eq "200" ] && body=$(sed "$d" <<< "$res") && echo "$body"; }
