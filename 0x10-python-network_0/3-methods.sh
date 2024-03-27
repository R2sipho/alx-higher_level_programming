#!/bin/bash
# Display all HTTP methods the server for this server.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
