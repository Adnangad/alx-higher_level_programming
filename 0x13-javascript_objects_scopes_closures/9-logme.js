#!/usr/bin/node
let ls = [];
exports.logMe = function (item) {
  ls.push(item);
  let idx = ls.indexOf(item);
  console.log(idx + ': ' + item);
};
