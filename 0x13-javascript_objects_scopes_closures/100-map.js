#!/usr/bin/node

const { list } = require("./100-data");
const lists = list.map((item, index) => item * index);
console.log(list);
console.log(lists);
