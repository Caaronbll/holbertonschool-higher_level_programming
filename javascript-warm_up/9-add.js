#!/usr/bin/node

let arg = process.argv.slice(2);
const arg1 = parseInt(arg[0]);
const arg2 = parseInt(arg[1]);

console.log(add(arg1, arg2));

function add (a, b) {
  return a + b;
}
