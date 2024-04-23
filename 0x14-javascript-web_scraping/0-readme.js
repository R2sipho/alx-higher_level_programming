#!/usr/bin/node

// Import the built-in Node.js 'fs' module.
const fs = require('fs');

// Use fs.readFile() to read the contents of a file specified as a command-line argument.
// 'utf8' specifies the encoding of the file being read.
fs.readFile(process.argv[2], 'utf8', function (error, content) {

  // If an error occurs during the file read operation, the 'error' parameter will contain an error object.
  if (error) {
    console.error('Error reading the file:', error);

  // If the file is read successfully, the 'content' parameter will contain the contents of the file as a string.
  } else {
    console.log(content);
  }
});

