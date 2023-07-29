#!/usr/bin/node

const [, , arg1] = process.argv;
const parsedInt = Number.parseInt(arg1, 10);

if (!Number.isNaN(parsedInt)) {
  console.log(`My number: ${parsedInt}`);
} else {
  console.log('Not a number');
}
