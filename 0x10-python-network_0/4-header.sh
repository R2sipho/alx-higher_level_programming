#!/bin/bash
# GET request to a given URL with  header variable.
curl -sH "X-School-User-Id: 98" "${1}"
