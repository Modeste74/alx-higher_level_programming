#!/usr/bin/node
exports.addMeMaybe = function incremental (number, theFunction) {
  const newValue = number + 1;
  theFunction(newValue);
};
