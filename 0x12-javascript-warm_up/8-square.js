#!/usr/bin/node

const x = process.argv[2];

if (!parseInt(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    let z = 0;
    let myVar = '';

    while (z < x) {
      myVar = myVar + 'X';
      z++;
    }
    console.log(myVar);
  }
}
