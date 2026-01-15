# JavaScript Functions Guide

Functions are one of the fundamental building blocks in JavaScript. This guide covers function declarations, expressions, arrow functions, control flow, scope, and practical application.

---

## 1. Function Definitions

JavaScript provides several ways to define functions, each with its own nuances regarding hoisting and syntax.

### Function Declaration
This is the traditional way to define a function. Function declarations are **hoisted**, meaning they can be called before they are defined in the code.

```javascript
// Function declarations are hoisted
sayHello(); // Output: Hello there!

function sayHello() {
    console.log("Hello there!");
}

function greet(name, lastName) {
    console.log(`Hello there ${name} ${lastName}`);
}

greet("John", "Doe"); // Output: Hello there John Doe
```

### Function Expression
Defining a function and assigning it to a variable. Function expressions are **not hoisted**, so they cannot be called before their definition.

```javascript
const add = function(a, b) {
    return a + b;
};

// addNumbers(5, 3); // Error: Cannot access 'addNumbers' before initialization
const addNumbers = function(num1, num2) {
    return num1 + num2;
};

console.log(addNumbers(5, 3)); // Output: 8
```

### Arrow Functions (ES6)
Introduced in ES6, arrow functions provide a shorter syntax and handle `this` keyword differently (lexical `this`). They are also **not hoisted**.

#### Basic Syntax
```javascript
const subtract = (a, b) => {
    return a - b;
};
console.log(subtract(10, 5)); // Output: 5
```

#### Implicit Return (Concise Body)
If the function body consists of a single expression, you can omit the curly braces `{}` and the `return` keyword.

```javascript
const multiply = (a, b) => a * b;
console.log(multiply(4, 2)); // Output: 8
```

#### Single Parameter
If there is exactly one parameter, the parentheses `()` around the parameter can be omitted.

```javascript
const square = x => x * x;
console.log(square(5)); // Output: 25
```

---

## 2. Parameters & Arguments

### Default Parameters
Allows parameters to be initialized with default values if no value or `undefined` is passed.

```javascript
function welcome(name = "Guest") {
    console.log(`Welcome, ${name}`);
}

welcome();       // Output: Welcome, Guest
welcome("John"); // Output: Welcome, John
```

### Rest Parameters (...)
Collects an indefinite number of arguments into an array.

```javascript
function sumAll(...numbers) {
    let total = 0;
    for (let num of numbers) {
        total += num;
    }
    return total;
}

console.log(sumAll(1, 2, 3, 4));     // Output: 10
console.log(sumAll(10, 20, 30, 40)); // Output: 100
```

---

## 3. Control Flow Statements

Efficient control flow is crucial for writing dynamic and responsive JavaScript applications.

### Conditionals

#### If / Else If / Else
Standard conditional logic for executing code based on conditions.

```javascript
let score = 85;

if (score >= 90) {
    console.log("Grade: A");
} else if (score >= 80) {
    console.log("Grade: B");
} else if (score >= 70) {
    console.log("Grade: C");
} else if (score >= 60) {
    console.log("Grade: D");
} else {
    console.log("Grade: F");
}
```

#### Ternary Operator
A concise way to write `if-else` statements, especially for assignments.
`condition ? valueIfTrue : valueIfFalse`

```javascript
let age = 20;
let canVote = age >= 18 ? "Yes" : "No";
console.log(canVote); // Output: Yes

const getForcast = temp => temp >= 70 ? "Warm" : "Cold";
console.log(getForcast(75)); // Output: Warm
```

#### Switch Statement
Used for handling multiple `if-else if` conditions in a more structured way, especially when comparing a single value against several possible cases.

```javascript
let dayNumber = 3; // 1 for Monday, 7 for Sunday
let dayName;

switch (dayNumber) {
    case 1:
        dayName = "Monday";
        break;
    case 2:
        dayName = "Tuesday";
        break;
    case 3:
        dayName = "Wednesday";
        break;
    case 4:
        dayName = "Thursday";
        break;
    case 5:
        dayName = "Friday";
        break;
    case 6:
        dayName = "Saturday";
        break;
    case 7:
        dayName = "Sunday";
        break;
    default:
        dayName = "Invalid Day";
}
console.log(dayName); // Output: Wednesday
```

### Loops

#### For Loop
The most common loop for iterating a known number of times.

```javascript
for (let i = 0; i < 5; i++) {
    console.log(i); // Output: 0, 1, 2, 3, 4
}
```

#### For...Of Loop
Iterates over iterable objects (like Arrays, Strings, Maps, Sets) directly, giving you the value of each element.

```javascript
const colors = ["red", "green", "blue"];
for (const color of colors) {
    console.log(color);
}
```

#### While Loop
Repeats a block of code as long as a specified condition is true.

```javascript
let count = 0;
while (count < 3) {
    console.log(count); // Output: 0, 1, 2
    count++;
}
```

#### Do...While Loop
Similar to a `while` loop, but guarantees that the block of code is executed at least once before the condition is tested.

```javascript
let i = 0;
do {
    console.log(i); // Output: 0
    i++;
} while (i < 0);
```

---

## 4. Scope

### Global Scope
Variables defined outside any function or block are in the global scope and are accessible from anywhere in the code.

```javascript
let globalVar = "I am global";

function test() {
    console.log(globalVar); // Accessible
}
test(); // Output: I am global
```

### Local (Function) Scope
Variables declared inside a function are in its local scope and are only accessible within that function.

```javascript
function testLocalScope() {
    let localVar = "I am local";
    console.log(localVar); // Accessible
}
testLocalScope(); // Output: I am local
// console.log(localVar); // Error: localVar is not defined
```

### Block Scope (`let` & `const`)
Variables declared with `let` and `const` inside a block (`{}`) are block-scoped, meaning they are only accessible within that block. `var` does not respect block scope.

```javascript
if (true) {
    let blockVar = "Hidden in block";
    var leakyVar = "Visible outside block"; // var ignores block scope
    console.log(blockVar); // Output: Hidden in block
}
// console.log(blockVar); // Error: blockVar is not defined
console.log(leakyVar); // Output: Visible outside block
```

---

## 5. Higher-Order Functions

Functions that take other functions as arguments (callbacks) or return them.

### Callback Example
```javascript
function processUser(name, callback) {
    console.log(`Processing ${name}...`);
    callback();
}

processUser("Alice", () => {
    console.log("Done processing Alice!");
});
// Output:
// Processing Alice...
// Done processing Alice!
```

### Array Methods as Higher-Order Functions
Modern JS relies heavily on higher-order functions for array manipulation.

```javascript
const nums = [1, 2, 3, 4, 5];

// map: Transforms each element and returns a new array
const doubled = nums.map(n => n * 2); 
console.log(doubled); // Output: [2, 4, 6, 8, 10]

// filter: Keeps elements that satisfy a condition and returns a new array
const evens = nums.filter(n => n % 2 === 0);
console.log(evens); // Output: [2, 4]

// forEach: Executes a function for each element (no return value)
nums.forEach(n => console.log(`Number: ${n}`));

// reduce: Reduces the array to a single value
const sum = nums.reduce((acc, curr) => acc + curr, 0);
console.log(sum); // Output: 15
```

---

## 6. Practical Exercises

Practice applying these concepts with the following exercises:

### Assignment: Geometry Calculations
1.  **Area of a Rectangle (Function Declaration):** Create a function `calculateArea(length, width)` that returns the area.
2.  **Perimeter of a Rectangle (Function Expression):** Create a function expression `calculatePerimeter` that returns the perimeter.
3.  **Diagonal of a Rectangle (Arrow Function):** Create an arrow function `calculateDiagonal(length, width)` that calculates the diagonal using `(length^2 + width^2)^0.5`.

```javascript
// Solutions
function calculateArea(length, width) {
    return length * width;
}

const calculatePerimeter = function(length, width) {
    return 2 * (length + width);
};

const calculateDiagonal = (length, width) => (length ** 2 + width ** 2) ** 0.5;

console.log("Area (5, 4):", calculateArea(5, 4)); // 20
console.log("Perimeter (5, 4):", calculatePerimeter(5, 4)); // 18
console.log("Diagonal (3, 4):", calculateDiagonal(3, 4)); // 5
```

### Assignment: Number & Season Checks
1.  **Number Classifier:** Create a function `checkNumber(number)` that returns "Positive", "Negative", or "Zero".
2.  **Season Detector:** Create a function `getSeason(month)` that takes a month number (1-12) and returns "Spring" (3-5), "Summer" (6-8), "Fall" (9-11), or "Winter" (12, 1-2).
3.  **Discount Calculator:** Create a function `calculateDiscount(age, price)`:
    *   If age <= 18, discount $10.
    *   If age >= 65, discount $20.
    *   Otherwise, no discount.

```javascript
// Solutions
function checkNumber(number) {
    if (number > 0) {
        return "Positive";
    } else if (number < 0) {
        return "Negative";
    } else {
        return "Zero";
    }
}

function getSeason(month) {
    if (month >= 3 && month <= 5) {
        return "Spring";
    } else if (month >= 6 && month <= 8) {
        return "Summer";
    } else if (month >= 9 && month <= 11) {
        return "Fall";
    } else {
        return "Winter";
    }
}

function calculateDiscount(age, price) {
    if (age <= 18) {
        return price - 10;
    } else if (age >= 65) {
        return price - 20;
    } else {
        return price;
    }
}

console.log("Check Number (5):", checkNumber(5));     // Positive
console.log("Check Number (-3):", checkNumber(-3));   // Negative
console.log("Check Number (0):", checkNumber(0));     // Zero
console.log("Season (4):", getSeason(4));             // Spring
console.log("Discount (15, 100):", calculateDiscount(15, 100)); // 90
console.log("Discount (70, 100):", calculateDiscount(70, 100)); // 80
console.log("Discount (30, 100):", calculateDiscount(30, 100)); // 100
```

---

## See Also

- [JavaScript Basics Cheat Sheet](../cheatsheets/JavaScript_Basics_Cheat_Sheet.md) - Core syntax and data types
- [JavaScript Objects and Arrays Cheat Sheet](../cheatsheets/JavaScript_Objects_Arrays_Cheat_Sheet.md) - Detailed guide on Objects and Arrays
- [JavaScript Async Programming Guide](JavaScript_Async_Programming_Guide.md) - Async functions and Promise patterns
- [DOM Manipulation Guide](DOM_Manipulation_Guide.md) - Using functions in event handlers and DOM operations
- [React Basics Guide](React_Basics_Guide.md) - Functions as React components
- [Functional Programming Cheat Sheet](../cheatsheets/Functional_Programming_Cheat_Sheet.md) - Concepts like map/filter/reduce