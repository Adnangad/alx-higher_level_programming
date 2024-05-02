#!/usr/bin/node
$(document).ready(function () {
  $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr', function (response) {
    const rez = response;
    $('DIV#hello').text('' + rez.hello);
  });
});
