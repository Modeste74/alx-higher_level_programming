#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

if (!isNaN(a) && !isNaN(b)) {
  const sum = add(a, b);
  console.log(sum);
} else {
  console.log('NaN');
}
