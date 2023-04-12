#!/usr/bin/node
// Adds two numbers parsed as argument to the program process.

const x = parseInt(process.argv[2]);
const y = parseInt(process.argv[3]);

function add (x, y) {
  const z = x + y;
  return z;
}

const result = add(x, y);
console.log(result);
