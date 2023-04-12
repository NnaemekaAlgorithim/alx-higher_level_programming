#!/usr/bin/node
// Keeps track of the number of arguments entered.

let count = 0;
exports.logMe = function (item) { console.log(`${count++}: ${item}`); };
