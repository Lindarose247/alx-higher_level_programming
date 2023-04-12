#!/usr/bin/node
const printingCIsFun = (x) => {
  if (isNaN(x)) {
    console.log('Missing number of occurrences');
  } else {
    let i = 0;
    while (i < x) {
      console.log('C is fun');
      i++;
    }
  }
};
