#!/usr/bin/node

const request = require('request');

// Check if the API URL argument is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./6-completed_tasks.js <API_URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];

// Make a GET request to the API URL
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Error:', response.statusCode);
    return;
  }

  // Parse the JSON response body
  const todos = JSON.parse(body);

  // Initialize an object to store the count of completed tasks for each user
  const completedTasksByUser = {};

  // Iterate through each task
  todos.forEach(todo => {
    // Check if the task is completed (completed property is true)
    if (todo.completed) {
      // Increment the count of completed tasks for the user
      if (completedTasksByUser[todo.userId]) {
        completedTasksByUser[todo.userId]++;
      } else {
        completedTasksByUser[todo.userId] = 1;
      }
    }
  });

  // Print the count of completed tasks for each user
  console.log(completedTasksByUser);
});

