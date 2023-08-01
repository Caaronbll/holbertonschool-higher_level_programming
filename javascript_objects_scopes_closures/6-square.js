#!/usr/bin/node

const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }
    const line = c.repeat(this.size);
    for (let i = 0; i < this.size; i++) {
      console.log(line);
    }
  }
}
module.exports = Square;
