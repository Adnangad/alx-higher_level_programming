#!/usr/bin/node
const url = process.argv[2];
const ful = 'https://swapi-api.alx-tools.com/api/films/' + `${url}`;
const request = require('request');
request(`${ful}`, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const films = JSON.parse(body);
  const actors = films.characters;
  for (const actor of actors) {
    const req = require('request');
    req(actor, function (error, response, body) {
      if (error) {
        console.error(error);
      }
      const act = JSON.parse(body);
      console.log(act.name);
    });
  }
});
