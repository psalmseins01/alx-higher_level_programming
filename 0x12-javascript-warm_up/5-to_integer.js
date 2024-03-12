#!/usr/bin/node
const checkNum = Math.floor(Number(process.argv[2]));
console.log(isNaN(checkNum) ? 'Not a number' : `My number: ${checkNum}`);
