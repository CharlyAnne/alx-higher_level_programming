#!/usr/bin/node
// script prints all characters of a start Wars movie

const request = require('request');
const movieID = process.argv[2];
const url = `https://swapi.dev/api/films/${movieID}/`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const content = JSON.parse(body);
  const characters = content.characters;
  for (const character of characters) {
    request(character, (error, body, response) => {
      if (error) {
        console.log(error);
        return;
      }
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  }
});
