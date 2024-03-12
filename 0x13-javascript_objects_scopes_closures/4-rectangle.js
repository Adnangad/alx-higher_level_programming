#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
      return;
    } else {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    let x = 0;
    while (x < this.height) {
      let y = 0;
      while (y < this.width) {
        process.stdout.write('X');
        y++;
      }
      process.stdout.write('\n');
      x++;
    }
  }

  rotate () {
    let temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = 2 * this.width;
    this.height = 2 * this.height;
  }
};
