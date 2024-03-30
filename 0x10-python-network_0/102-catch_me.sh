#!/bin/bash
# causes serever to respond with a specific message
curl -o /dev/null -sw "You got me!" 0.0.0.0:5000/catch_me
