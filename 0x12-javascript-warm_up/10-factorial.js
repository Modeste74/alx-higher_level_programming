#!/usr/bin/node
function factorial (n) {
  if (isNaN(n)) {
    return 1;
  }
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
const Arg = parseInt(process.argv[2]);
const result = factorial(Arg);
console.log(result);
