#!/usr/bin/node
const fileName = process.argv[2];
const cont = process.argv[3];
const fs = require('fs');
fs.writeFile(`${fileName}`, `${cont}`, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
