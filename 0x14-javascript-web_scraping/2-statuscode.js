#!/usr/bin/node
const request = require('request');
const server_addr = process.argv[2];

request.get(server_addr, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
