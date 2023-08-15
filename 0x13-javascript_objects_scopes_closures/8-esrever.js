#!/usr/bin/node
exports.esrever = function (list) {
  let startIndex = 0;
  let endIndex = list.length - 1;
  while (startIndex < endIndex) {
    const temp = list[startIndex];
    list[startIndex] = list[endIndex];
    list[endIndex] = temp;
    startIndex++;
    endIndex--;
  }
  return list;
};
