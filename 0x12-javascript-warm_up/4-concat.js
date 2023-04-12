#!/usr/bin/node
function printArguments(arg1, arg2) {
  // Check if both arguments are provided
  if (arg1 === undefined || arg2 === undefined) {
    console.error('Error: Two arguments must be provided');
    return;
  }

  // Print arguments in the required format
  console.log(`${arg1} is ${arg2}`);
}
