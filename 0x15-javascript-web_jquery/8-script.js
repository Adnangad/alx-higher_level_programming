#!/usr/bin/node
$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  method: 'GET',
  success: function (response) {
    $.each(response.results, function (index, film) {
      $('UL#list_movies').append('<li>' + film.title + '</li>');
    });
  }
});
