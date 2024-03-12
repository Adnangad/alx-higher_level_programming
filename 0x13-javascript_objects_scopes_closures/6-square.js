#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let x = 0;
      while (x < this.height) {
        let y = 0;
        while (y < this.width) {
          process.stdout.write(c);
          y++;
	}
        process.stdout.write('\n');
        x++;
      }
  }
};
