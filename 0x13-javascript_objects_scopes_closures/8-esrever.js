#!/usr/bin/node
exports.esrever = function (list) {
  let x = 0;
  let j = list.length - 1;
  while (x < j) {
      let temp = list[x];
      list[x] = list[j];
      list[j] = temp;
      j--;
      x++;
    }
  return list;
};
