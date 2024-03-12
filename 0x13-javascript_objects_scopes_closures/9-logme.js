#!/usr/bin/node
const ls = [];
exports.logMe = function (item) {
  ls.push(item);
  const idx = ls.indexOf(item);
  console.log(idx + ': ' + item);
};
