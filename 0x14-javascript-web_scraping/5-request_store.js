#!/usr/bin/node

// Import the built-in Node.js 'fs' module for file system operations
const fs = require('fs');

// Import the 'request' module for making HTTP GET requests
const request = require('request');

// Use the 'request' module to perform an HTTP GET request to the URL provided as the first command-line argument
// The response is piped directly to a file using the 'fs' module's createWriteStream method, with the filename provided as the second command-line argument
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));

