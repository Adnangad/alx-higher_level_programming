#!/usr/bin/node
const url = process.argv[2];
const fileName = process.argv[3];
const request = require('request');
request(`${url}`, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const data = body;
  const fs = require('fs');
  fs.writeFile(`${fileName}`, data, 'utf8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
