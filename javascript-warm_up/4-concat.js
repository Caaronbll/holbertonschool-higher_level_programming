#!/usr/bin/node

const arguments = proccess.argv.slice(2);
let arg1, arg2;
if (arguments[0]) {
    arg1 = arguments[0];
} else {
    arg1 = 'undefined';
}
if (arguments[1]) {
    arg2 = arguments[1];
} else {
    arg2 = 'undefined';
}
console.log(arg1 + ' is ' + arg2);
