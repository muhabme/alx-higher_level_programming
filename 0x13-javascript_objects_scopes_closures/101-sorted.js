#!/usr/bin/node
const dict = require('./101-data').dict;

const entries = Object.entries(dict);
const values = Object.values(dict);
const uniqueValues = [...new Set(values)];
const newDict = {};
for (const j in uniqueValues) {
  const list = [];
  for (const k in entries) {
    if (entries[k][1] === uniqueValues[j]) {
      list.unshift(entries[k][0]);
    }
  }
  newDict[uniqueValues[j]] = list;
}
console.log(newDict);
