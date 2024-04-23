#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API endpoint
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    // Parse the JSON response body
    const data = JSON.parse(body);

    // Print the title of the movie if data is found
    if (data.title) {
      console.log(data.title);
    } else {
      console.error('Movie not found.');
    }
  }
});

