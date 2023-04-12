#!/usr/bin/node
// This code prints C is fun in x number of times

const argnt = process.argv;
const i = parseInt(argnt[2]);

if (isNaN(i)) {
  console.log('Missing number of occurrences');
} else {
  for (let j = 0; j < i; j++) {
    console.log('C is fun');
  }
}
