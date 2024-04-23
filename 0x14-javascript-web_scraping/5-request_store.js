#!/usr/bin/node

// Import the built-in Node.js 'fs' module
const fs = require('fs');

// Import the 'request' module
const request = require('request');

// Check if the command-line arguments are provided correctly
if (process.argv.length !== 4) {
  console.error('Usage: ./script.js <url> <filename>');
  process.exit(1);
}

// Extract URL and filename from command-line arguments
const url = process.argv[2];
const filename = process.argv[3];

// Use the 'request' module to perform an HTTP GET request to the URL
request(url)
  // Pipe the response directly to a file using the 'fs' module
  .pipe(fs.createWriteStream(filename))
  // Handle errors during the request
  .on('error', (error) => {
    console.error('Error:', error);
  })
  // Notify the user when the download is complete
  .on('finish', () => {
    console.log(`File '${filename}' downloaded successfully.`);
  });

