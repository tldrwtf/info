# JavaScript Functions Guide

Functions are one of the fundamental building blocks in JavaScript. This guide covers function declarations, expressions, arrow functions, and scope.

## 1. Function Syntax

### Function Declaration
The traditional way to define a function. These are **hoisted** (can be called before they are defined).

```javascript
function greet(name) {
    return `Hello, ${name}!`;
}

console.log(greet("Alice")); // "Hello, Alice!"
```

### Function Expression
Defining a function inside a variable. These are **not hoisted**.

```javascript
const add = function(a, b) {
    return a + b;
};

console.log(add(5, 3)); // 8
```

---

## 2. Arrow Functions (ES6)

A shorter syntax for writing functions. Commonly used for callbacks.

### Basic Syntax
```javascript
const subtract = (a, b) => {
    return a - b;
};
```

### Implicit Return
If the function body is a single expression, you can remove the `{}` and `return`.

```javascript
const multiply = (a, b) => a * b;

console.log(multiply(4, 2)); // 8
```

### Single Parameter
If there is exactly one parameter, you can remove the `()`.

```javascript
const square = x => x * x;
```

---

## 3. Parameters & Arguments

### Default Parameters
```javascript
function welcome(name = "Guest") {
    console.log(`Welcome, ${name}`);
}

welcome(); // "Welcome, Guest"
welcome("John"); // "Welcome, John"
```

### Rest Parameters (...)
Collects multiple arguments into an array.

```javascript
function sumAll(...numbers) {
    let total = 0;
    for (let num of numbers) {
        total += num;
    }
    return total;
}

console.log(sumAll(1, 2, 3, 4)); // 10
```

---

## 4. Scope

### Global Scope
Variables defined outside any function or block.

```javascript
let globalVar = "I am global";

function test() {
    console.log(globalVar); // Accessible
}
```

### Local (Function) Scope
Variables defined inside a function.

```javascript
function test() {
    let localVar = "I am local";
}
// console.log(localVar); // Error: localVar is not defined
```

### Block Scope (`let` & `const`)
Variables defined inside `{}` (if statements, loops) are only accessible there.

```javascript
if (true) {
    let blockVar = "Hidden";
    var leakyVar = "Visible"; // var ignores block scope (Avoid!)
}
// console.log(blockVar); // Error
console.log(leakyVar); // "Visible"
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
    console.log("Done!");
});
```

### Array Methods
Modern JS relies heavily on higher-order functions for arrays.

```javascript
const nums = [1, 2, 3, 4, 5];

// map: transform each element
const doubled = nums.map(n => n * 2); 
// [2, 4, 6, 8, 10]

// filter: keep elements that match condition
const evens = nums.filter(n => n % 2 === 0);
// [2, 4]

// forEach: loop through (no return)
nums.forEach(n => console.log(n));
```

---

## See Also

- **[JavaScript Basics Cheat Sheet](./JavaScript_Basics_Cheat_Sheet.md)** - Core syntax and data types
- **[Functional Programming Cheat Sheet](./Functional_Programming_Cheat_Sheet.md)** - Concepts like map/filter/reduce (Python context, but relevant)
- **[Data Structures Cheat Sheet](./Data_Structures_Cheat_Sheet.md)** - General data structure concepts