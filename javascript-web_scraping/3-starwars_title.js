#!/usr/bin/node

const fs = require('request');
let url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function(error, response, body) {
  console.log(error || JSON.parse(body).title);
});
