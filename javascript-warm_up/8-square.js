#!/usr/bin/node

const arg = process.argv.slice(2);
const size = arg[0];
let outline = '';
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let y = 0; y < size; y++) {
    outline += 'X';
  }
  for (let x = 0; x < size; x++) {
    console.log(outline);
  }
}
