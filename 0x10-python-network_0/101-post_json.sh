#!/bin/bash
# Send POST request and display response body
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
