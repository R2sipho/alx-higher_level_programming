#!/usr/bin/node
const argv = process.argv;
const x = parseInt(argv[2]);
if (isNaN(x)) {
  console.log('Missing size');
} else {
  const character = 'X';
  const line = character.repeat(x);
  for (let i = 0; i < x; i++) {
    console.log(line);
  }
}
