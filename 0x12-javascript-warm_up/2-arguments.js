#!/usr/bin/node
let no_arg = process.argv.length;

if (no_arg < 3) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
