#!/usr/bin/node
const Parentsquare = require('./5-square');
module.exports = class Square extends Parentsquare {
  /*constructor (size) {
    super(size);
  }*/
  charprint(c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let row = '';
        for (let j = 0; j < this.width; j++) {
          row += 'C';
	}
      console.log(row);
      }
    }
}
};
