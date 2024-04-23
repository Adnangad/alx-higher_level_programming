#!/usr/bin/node
const url = 'https://swapi-api.alx-tools.com/api/films/';
const req = process.argv[2];
const ful = `${url}` + `${req}`;
const request = require('request');
request(`${ful}`, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const movie = JSON.parse(body);
  console.log(movie.title);
});
