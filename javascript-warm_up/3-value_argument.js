#!/usr/bin/node

const [, argument] = process.argv;

if (argument) {
  console.log(argument);
} else {
  console.log("No argument");
}
