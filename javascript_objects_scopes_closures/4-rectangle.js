#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let count = '';
    for (let x = 0; x < this.width; x++) {
      count += 'X';
    }
    for (let y = 0; y < this.height; y++) {
      console.log(count);
    }
  }

  rotate () {
    const holder = this.height;
    this.height = this.width;
    this.width = holder;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}
module.exports = Rectangle;
