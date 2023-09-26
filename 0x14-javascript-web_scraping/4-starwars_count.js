#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const filterUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const filmData = JSON.parse(body);
    const eightEen = filmData.results;
    const filterData = eightEen.filter(film => film.characters.includes(filterUrl));
    console.log(`${filterData.length}`);
  }
});
