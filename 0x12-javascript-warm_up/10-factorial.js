#!/usr/bin/node
// This code calculates the factorial of the number parsed as argument to it.

function factorial (num) {
  if (isNaN(num) || num < 2) return 1;
  else return num * factorial(num - 1);
}

console.log(factorial(process.argv[2]));
