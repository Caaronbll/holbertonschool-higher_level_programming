#!/usr/bin/node

import { argv } from 'node:process';

let argcount = 0;
argv.forEach((val, index) => {
    argcount =+ 1;
  });

if (argcount == 0){
    console.log('No argument');
}
else if (argcount == 1){
    console.log('No argument');
}
else if (argcount > 1){
    console.log('Arguments found')
}
