#!/usr/bin/node
const url = process.argv[2];
const ful = `${url}`;
const answ = 'https://swapi-api.alx-tools.com/api/people/18/';
const request = require('request');
request(`${ful}`, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  let count = 0;
  const films = JSON.parse(body).results;
  for (const film of films) {
    const actors = film.characters;
    for (const actor of actors) {
      if (actor === `${answ}`) {
        count += 1;
      }
    }
  }
  console.log(count);
});
