#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  const charrPromises = characters.map(charrUrl => {
    return new Promise((resolve, reject) => {
      request(charrUrl, (error, response, body) => {
        if (error) {
          reject(error);
          return;
        }
        const charrData = JSON.parse(body);
        resolve(charrData.name);
      });
    });
  });

  Promise.all(charrPromises)
    .then(charrnames => {
      charrnames.forEach(charrname => console.log(charrname));
    })
    .catch(error => console.error(error));
});
