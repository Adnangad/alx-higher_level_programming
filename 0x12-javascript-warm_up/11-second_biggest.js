#!/usr/bin/node
function secondBigest (array) {
  let i = 0;
  while (i < array.length) {
    let j = 0;
    while (j < array.length - 1) {
      if (array[j] > array[j + 1]) {
        const temp = array[j];
        array[j] = array[j + 1];
        array[j + 1] = temp;
      }
      j++;
    }
    i++;
  }
  return array;
}
const args = process.argv.slice(2).map(Number);
if (args.length <= 1) {
  console.log(0);
} else {
  const sot = secondBigest(args);
  console.log(sot[sot.length - 2]);
}
