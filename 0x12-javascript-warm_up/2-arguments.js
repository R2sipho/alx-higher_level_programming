#!/usr/bin/node

const argumentCount = process.argv.length;

switch (argumentCount) {
  case 2:
    console.log('No argument');
    break;
  case 3:
    console.log('Argument found');
    break;
  default:
    console.log('Arguments found');
    break;
}
