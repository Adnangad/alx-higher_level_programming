#!/usr/bin/node
exports.converter = function (base) {
  return function convert (x) {
    if (x === 0) {
      return '';
    }
    return x.toString(base);
  };
};
