#!/usr/bin/node
/* script prints the number of movies where the character
 * “Wedge Antilles” is present */
const request = require('request');
const url = process.argv[2];
const characterID = '18';
let count = 0;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    JSON.parse(body).results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(characterID)) {
          count += 1;
        }
      });
    });
    console.log(count);
  }
});
