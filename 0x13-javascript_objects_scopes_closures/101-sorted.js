#!/usr/bin/node
cost dict = require('./101-data.js').dict;
const newDict = {};
let key;
for (key in dict) {
  if (dict[key] in newDict) {
    newDict[dict[key]].push(key);
  } else {
    newDict[dict[key]] = [key];
  }
}
console.log(newDict);
