#!/usr/bin/node
module.exports = class Rectanngle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let a = this.height;
    while (a) {
      console.log('X'.repeat(this.width));
      a--;
    }
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }

  rotate () {
    const change = this.width;
    this.width = this.height;
    this.height = change;
  }
};
