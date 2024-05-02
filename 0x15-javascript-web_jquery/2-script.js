#!/usr/bin/node
const temp = $('DIV#red_header');
temp.on('click', function () {
  const el = $('header');
  el.css('color', '#FF0000');
});
