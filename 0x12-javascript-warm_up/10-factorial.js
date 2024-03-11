#!/usr/bin/node
function factorial (n) {
  if (n >= 1) {
    return n * (factorial(n - 1));
  } else {
    return 1;
  }
}
const val = parseInt(process.argv[2]);
if (isNaN(val)) {
  console.log(1);
} else {
  console.log(factorial(val));
}
