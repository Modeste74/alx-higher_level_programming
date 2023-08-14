#!/usr/bin/node
if (process.argv.length < 3) {
  console.log(0);
} else {
  const store = [];
  for (let i = 2; i < process.argv.length; i++) {
    const values = parseInt(process.argv[i]);
    store.push(values);
  }
  if (store.length === 1) {
    console.log(0);
  } else {
    store.sort((a, b) => b - a);
    console.log(store[1]);
  }
}
