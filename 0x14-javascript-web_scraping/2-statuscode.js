#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
if (!url) {
  console.error('pass the url to GET');
  process.exit(1);
}
request.get(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
