#!/usr/bin/node

// Import the 'request' module.
const request = require('request');

// Use the 'request' module to perform an HTTP GET request to the URL specified as the first command-line argument.
request.get(process.argv[2])

  // Set up an event listener for the 'response' event emitted by the HTTP request.
  .on('response', function (response) {

    // Log the HTTP status code of the response to the console.
    console.log(`code: ${response.statusCode}`);
  });

