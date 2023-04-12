#!/usr/bin/node
// This code prints a square using X based on the value of argument passed

if (isNaN(process.argv[2])) {
  console.log('Missing value of size');
} else if (parseInt(process.argv[2]) > 0) {
  for (let j = 0; j < parseInt(process.argv[2]); j++) {
    console.log('X'.repeat(parseInt(process.argv[2])));
  }
}
