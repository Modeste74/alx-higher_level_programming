#!/usr/bin/node
const array1 = require('./100-data');
const intialList = array1.list;
const newList = intialList.map((value, index) => value * index);
console.log(intialList);
console.log(newList);
