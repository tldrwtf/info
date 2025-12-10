// Practice_Solutions/JavaScript/JavaScript_Array_Manipulation_Solutions.js

// Task 15.3: Array Manipulation

let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// 1. Filter out odd numbers (keep only evens)
const evens = numbers.filter(num => num % 2 === 0);
console.log("Even numbers:", evens); // Expected: [2, 4, 6, 8, 10]

// 2. Map the remaining numbers to their squares
const squares = evens.map(num => num * num);
console.log("Squares of evens:", squares); // Expected: [4, 16, 36, 64, 100]

// 3. Log the final array
console.log("\nFinal array after filtering and mapping:", squares);
