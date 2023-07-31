#!/usr/bin/node

function findSecondBiggestInteger (...args) {
  if (args.length <= 1) {
    return 0;
  }

  let biggest = -Infinity;
  let secondBiggest = -Infinity;

  for (const arg of args) {
    const num = parseInt(arg);

    if (num > biggest) {
      secondBiggest = biggest;
      biggest = num;
    } else if (num > secondBiggest && num !== biggest) {
      secondBiggest = num;
    }
    }

  return secondBiggest;
}

// Get command-line arguments and pass them to the function
const args = process.argv.slice(2);
const secondBiggest = findSecondBiggestInteger(...args);

// Print the result
console.log(secondBiggest);
