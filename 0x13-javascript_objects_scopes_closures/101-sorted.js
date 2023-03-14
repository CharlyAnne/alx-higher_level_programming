#!/usr/bin/node
const dict = require('./101-data').dict;

const newDictOccurrence = {};
for (const [key, value] of Object.entries(dict)) {
  if (newDictOccurrence[value]) {
    newDictOccurrence[value].push(key);
  } else {
    (newDictOccurrence[value] = [key]);
  }
}
console.log(newDictOccurrence);
