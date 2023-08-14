#!/usr/bin/node
exports.callMeMoby = function executeXtimes (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
