#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
<<<<<<< HEAD
  if (w > 0 && h > 0) {
    this.width = w;
    this.height = h;
  }
=======
    if (w >= 0 || h >= 0) {
      this.width = w;
      this.height = h;
    }
>>>>>>> c8bdf00f61d18edf0ca59786c326182b6b0b8899
  }
}
module.exports = Rectangle;
