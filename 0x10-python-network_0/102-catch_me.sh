#!/bin/bash

# Send a PUT request with the specified data to the server
curl -s -X PUT -L -d "user_id=98" 0.0.0.0:5000/catch_me

