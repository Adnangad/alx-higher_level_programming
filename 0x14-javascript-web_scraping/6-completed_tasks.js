#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
request(`${url}`, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const dict = {};
  const data = JSON.parse(body);
  for (const dat of data) {
    if (dat.completed === true) {
      if (dict[dat.userId]) {
        dict[dat.userId] += 1;
      } else {
        dict[dat.userId] = 1;
      }
    }
  }
  console.log(dict);
});
