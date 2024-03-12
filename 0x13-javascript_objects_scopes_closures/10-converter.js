#!/usr/bin/node
exports.converter = function (base) {
  return function convert (x) {
    return x.toString(base);
  };
};
