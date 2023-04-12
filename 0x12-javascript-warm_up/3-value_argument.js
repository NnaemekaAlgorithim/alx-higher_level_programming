#!/usr/bin/node

// This code checks if an argument was passed and prints no argument if none or the value of the first arguement

if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
