#!/usr/bin/node

// Import the 'request' module
const request = require('request');

// Use the 'request' module to perform an HTTP GET request to the URL
request(process.argv[2], function (error, response, body) {
  // Check if there was no error during the HTTP request.
  if (!error) {
    // Parse the JSON data
    const data = JSON.parse(body);
    
    // Check if the data contains any movies
    if (data.results.length > 0) {
      // Iterate through the movies in the 'results' array.
      for (const movie of data.results) {
        // Check if there is a character with ID 18 ('/18/') in the 'characters' array.
        if (movie.characters.some(character => character.endsWith('/18/'))) {
          // If a character with ID 18 is found, print the title of the movie and break the loop.
          console.log(movie.title);
          break;
        }
      }
    } else {
      console.error('No movies found.');
    }
  } else {
    console.error('Error:', error);
  }
});

