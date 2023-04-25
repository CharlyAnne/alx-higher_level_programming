#!/usr/bin/node
/* script gets the content of a webpage and stores it
 * in a file */
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filename = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(filename, body, 'utf-8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
