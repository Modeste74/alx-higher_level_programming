#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  const movieData = JSON.parse(body);
  const characterUrls = movieData.characters;
  const fetchCharacter = (url) => {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
          return;
        }
        const characterData = JSON.parse(body);
        resolve(characterData.name);
      });
    });
  };
  const fetchAllCharacters = async () => {
    for (const url of characterUrls) {
      const characterName = await fetchCharacter(url);
      console.log(characterName);
    }
  };
  fetchAllCharacters();
});
