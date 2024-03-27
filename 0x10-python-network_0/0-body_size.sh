#!/bin/bash
res=$(curl -sS "$1")
echo -n "$res" | wc -c
