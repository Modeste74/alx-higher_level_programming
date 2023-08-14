#!/usr/bin/node
const noArg = process.argv.length;

if (noArg < 3) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
