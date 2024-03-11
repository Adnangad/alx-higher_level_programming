#!/usr/bin/node
const x = parseInt(process.argv[2]);
let i = 0;
if (isNaN(x)) {
  console.log('Missing size');
} else {
  while (i < x) {
    let j = 0;
    while (j < x) {
      process.stdout.write('X');
      j++;
    }
    process.stdout.write('\n');
    i++;
  }
}
