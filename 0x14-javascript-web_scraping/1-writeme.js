#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const stringTowrite = process.argv[3];
if (!filePath || !stringTowrite) {
  console.error('Provide file path and string');
  process.exit(1);
}
fs.writeFile(filePath, stringTowrite, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
