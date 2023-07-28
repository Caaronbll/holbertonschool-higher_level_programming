#!/usr/bin/node

const argcount = process.argv.length;

if (argcount === 0){
  console.log('No argument');
}
else if (argcount === 1){
  console.log('Argument found');
}
else if (argcount > 1){
  console.log('Arguments found')
}
