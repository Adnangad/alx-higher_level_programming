#!/bin/bash
# Displays te response of a request of an url
echo -n "$(curl -sS "$1")" | wc -c
