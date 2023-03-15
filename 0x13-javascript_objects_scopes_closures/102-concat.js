//#!/usr/bin/node

const fs = require('fs');

const str1 = fs.readFileSync(process.argv[2], 'utf8');
const str2 = fs.readFileSync(process.argv[3], 'utf8');
const str3 = str1 + str2;
fs.writeFile(process.argv[4], str3, (err) => {
    if (err) {
        throw err;
   }
});