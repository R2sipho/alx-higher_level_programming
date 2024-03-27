#!/bin/bash
# Check if URL argument is provided
curl -sI GET "$1" | grep -i "Content-Length" | cut -d " " -f2
