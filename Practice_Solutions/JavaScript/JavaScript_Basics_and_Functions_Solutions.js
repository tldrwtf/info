// Practice_Solutions/JavaScript/JavaScript_Basics_and_Functions_Solutions.js

// Task 15.1: Hello World & Variables
console.log("Hello, World!");

let name = "Allan"; // Replace with your name
console.log(`Hello, ${name}!`);

// Task 15.2: Simple Calculator
const calculate = (num1, num2, operation) => {
    switch (operation) {
        case "+":
            return num1 + num2;
        case "-":
            return num1 - num2;
        case "*":
            return num1 * num2;
        case "/":
            if (num2 === 0) {
                return "Error: Division by zero";
            }
            return num1 / num2;
        default:
            return "Error: Invalid operation";
    }
};

console.log("\n--- Calculator Tests ---");
console.log(`5 + 3 = ${calculate(5, 3, "+")}`);   // Expected: 8
console.log(`10 - 4 = ${calculate(10, 4, "-")}`); // Expected: 6
console.log(`7 * 6 = ${calculate(7, 6, "*")}`);   // Expected: 42
console.log(`10 / 2 = ${calculate(10, 2, "/")}`); // Expected: 5
console.log(`10 / 0 = ${calculate(10, 0, "/")}`); // Expected: Error: Division by zero
console.log(`10 % 3 = ${calculate(10, 3, "%" )}`); // Expected: Error: Invalid operation
