#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = (dict) => {
  const newDiction = {};
  for (const key in dict) {
    if (newDiction[dict[key]] === undefined) {
      newDiction[dict[key]] = [];
    }
    newDiction[dict[key]].push(key);
  }
  return newDiction;
};
console.log(newDict(dict));
