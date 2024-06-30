#!/usr/bin/node

const { dict } = require('./101-data');
const newDict = {};
for (const key in dict) {
  if (newDict[dict[key]]) newDict[dict[key]].push(key);
  else newDict[dict[key]] = [key];
}
console.log(newDict);
