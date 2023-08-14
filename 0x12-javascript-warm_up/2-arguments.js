#!/usr/bin/node
const noArg = process.argv.length;

if (noArg < 3) {
  console.log('No argument');
} else if (noArg < 4) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
