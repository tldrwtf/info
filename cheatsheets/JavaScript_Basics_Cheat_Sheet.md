# JavaScript Basics Cheat Sheet

**JavaScript (JS)** is a lightweight, interpreted programming language with first-class functions. It is best known as the scripting language for Web pages.

---

## Variable Declarations

Modern JavaScript uses `let` and `const`. Avoid `var` for new code.

### `var` (Legacy)
*   Function-scoped.
*   Can be redeclared and updated.
*   Hoisted to the top of its function or global scope, initialized with `undefined`.

```javascript
var oldWay = 10;
var oldWay = 20; // No error
oldWay = 30;     // Can be updated
console.log(oldWay); // 30
```

### `let` (Modern)
*   Block-scoped.
*   Can be updated but not redeclared within the same block.
*   Hoisted, but not initialized (`Temporal Dead Zone`) until declared.

```javascript
let age = 25;
// let age = 26; // Error: Cannot redeclare block-scoped variable
age = 26;      // OK
console.log(age); // 26

if (true) {
    let blockScoped = "I live in this block";
    console.log(blockScoped); // "I live in this block"
}
// console.log(blockScoped); // Error: blockScoped is not defined
```

### `const` (Modern, for constants)
*   Block-scoped.
*   Cannot be redeclared or updated. Must be initialized at declaration.
*   Hoisted, but not initialized (`Temporal Dead Zone`) until declared.

```javascript
const pi = 3.14;
// const pi = 3.14159; // Error: Cannot redeclare block-scoped variable
// pi = 3.14159;      // Error: Assignment to constant variable
console.log(pi); // 3.14

const person = { name: "Alice" };
person.name = "Bob"; // OK: Can modify properties of a const object
// person = { name: "Charlie" }; // Error: Assignment to constant variable
```

## Data Types

| Type | Example | Description |
| :--- | :--- | :--- |
| **String** | `"Hello"`, `'Hi'`, `` `Yo` `` | Text data. |
| **Number** | `42`, `3.14` | Integers and floats are one type (`double-precision 64-bit binary format`). |
| **Boolean** | `true`, `false` | Logical values. |
| **Null** | `null` | Intentional absence of value. |
| **Undefined** | `undefined` | Variable declared but not assigned. |
| **Symbol** | `Symbol('id')` | Unique and immutable primitive value. |
| **BigInt** | `10n` | For integers larger than `2^53 - 1`. |
| **Object** | `{ key: "value" }`, `[1, 2, 3]`, `null` | Key-value pairs, arrays, functions, dates, etc. (everything else). |

## Operators

### Arithmetic Operators
Perform mathematical calculations.

| Operator | Description    | Example      | Result |
| :------- | :------------- | :----------- | :----- |
| `+`      | Addition       | `10 + 5`     | `15`   |
| `-`      | Subtraction    | `10 - 5`     | `5`    |
| `*`      | Multiplication | `10 * 5`     | `50`   |
| `/`      | Division       | `10 / 5`     | `2`    |
| `%`      | Modulus        | `10 % 3`     | `1`    |
| `**`     | Exponentiation | `2 ** 3`     | `8`    |
| `++`     | Increment      | `let x=5; x++` | `x` becomes `6` |
| `--`     | Decrement      | `let y=5; y--` | `y` becomes `4` |

### Comparison Operators
Compare two values and return a boolean.

| Operator | Description                  | Example        | Result  |
| :------- | :--------------------------- | :------------- | :------ |
| `==`     | Loose Equality (value only)  | `5 == "5"`     | `true`  |
| `===`    | Strict Equality (type & value)| `5 === "5"`    | `false` |
| `!=`     | Loose Inequality             | `5 != "5"`     | `false` |
| `!==`    | Strict Inequality            | `5 !== "5"`    | `true`  |
| `>`      | Greater than                 | `10 > 5`       | `true`  |
| `<`      | Less than                    | `10 < 5`       | `false` |
| `>=`     | Greater than or equal to     | `10 >= 10`     | `true`  |
| `<=`     | Less than or equal to        | `10 <= 5`      | `false` |

### Logical Operators
Combine boolean expressions.

| Operator | Description                                     | Example               | Result  |
| :------- | :---------------------------------------------- | :-------------------- | :------ |
| `&&`     | AND (returns `true` if both operands are `true`)| `true && false`       | `false` |
| `\|\|`    | OR (returns `true` if at least one is `true`)   | `true \|\| false`      | `true`  |
| `!`      | NOT (inverts the boolean value)                 | `!true`               | `false` |

### Assignment Operators
Assign values to variables.

| Operator | Example      | Equivalent to |
| :------- | :----------- | :------------ |
| `=`      | `x = 10`     | `x = 10`      |
| `+=`     | `x += 5`     | `x = x + 5`   |
| `-=`     | `x -= 5`     | `x = x - 5`   |
| `*=`     | `x *= 5`     | `x = x * 5`   |
| `/=`     | `x /= 5`     | `x = x / 5`   |
| `%=`     | `x %= 3`     | `x = x % 3`   |
| `**=`    | `x **= 3`    | `x = x ** 3`  |

## String Methods

Strings are immutable in JavaScript, meaning string methods return a new string rather than modifying the original.

```javascript
let message = "  Hello, World!  ";

console.log(message.length);          // 17
console.log(message.trim());          // "Hello, World!"
console.log(message.toUpperCase());   // "  HELLO, WORLD!  "
console.log(message.toLowerCase());   // "  hello, world!  "
console.log(message.indexOf("World"));// 9 (index of first occurrence)
console.log(message.includes("Hello"));// true
console.log(message.slice(2, 7));     // "Hello" (start, end_exclusive)
console.log(message.replace("World", "Universe")); // "  Hello, Universe!  "

let greeting = "Hi";
let name = "Alice";
console.log(greeting.concat(", ", name, "!")); // "Hi, Alice!"
```

## Console Output

```javascript
console.log("Hello, World!");
console.error("Something went wrong");
console.warn("Warning!");
console.info("Information message");
console.table([{a:1, b:2}, {a:3, b:4}]); // Displays tabular data
```

## Template Literals

Use backticks (`` ` ``) for string interpolation (like Python f-strings) and multi-line strings.

```javascript
let name = "Alice";
let greeting = `Hello, ${name}!
Welcome to JavaScript.`;
console.log(greeting);
```

---

## Control Flow

### Conditionals

#### If / Else
```javascript
let score = 85;

if (score >= 90) {
    console.log("A");
} else if (score >= 80) {
    console.log("B");
} else if (score >= 70) {
    console.log("C");
} else if (score >= 60) {
    console.log("D");
} else {
    console.log("F");
}
```

#### Ternary Operator
`condition ? valueIfTrue : valueIfFalse`

```javascript
let age = 20;
let canVote = age >= 18 ? "Yes" : "No";
console.log(canVote); // "Yes"
```

#### Switch Statement
```javascript
let fruit = "apple";

switch (fruit) {
    case "banana":
        console.log("Yellow");
        break;
    case "apple":
        console.log("Red");
        break; // Don't forget break!
    default:
        console.log("Unknown fruit");
}
```

### Loops

#### For Loop (Standard)
```javascript
for (let i = 0; i < 5; i++) {
    console.log(i); // 0, 1, 2, 3, 4
}
```

#### For...Of (Iterating over iterable collections like Arrays, Strings)
```javascript
const colors = ["red", "green", "blue"];
for (const color of colors) {
    console.log(color);
}

const myString = "hello";
for (const char of myString) {
    console.log(char);
}
```

#### For...In (Iterating over object properties)
```javascript
const car = { make: "Toyota", model: "Camry" };
for (const key in car) {
    console.log(`${key}: ${car[key]}`);
}
// Output:
// make: Toyota
// model: Camry
```

#### While Loop
```javascript
let count = 0;
while (count < 3) {
    console.log(count); // 0, 1, 2
    count++;
}

let i = 0;
do {
    console.log(i); // Guaranteed to run at least once
    i++;
} while (i < 0); // Only runs once
```

---

## Type Coercion and Truthiness

JavaScript can perform implicit type conversion (coercion), which can lead to unexpected results, especially with loose equality (`==`). Values can also be "truthy" or "falsy" in boolean contexts.

### Falsy Values
*   `false`
*   `0` (number zero)
*   `-0` (negative zero)
*   `0n` (BigInt zero)
*   `""` (empty string)
*   `null`
*   `undefined`
*   `NaN` (Not-A-Number)

All other values are considered **truthy**.

```javascript
if ("hello") {
    console.log("This is truthy"); // This runs
}

if (0) {
    console.log("This is falsy"); // This does not run
}

if (null == undefined) {
    console.log("Null and Undefined are loosely equal"); // This runs
}

if (null === undefined) {
    console.log("Null and Undefined are strictly equal"); // This does not run
}
```

---

## See Also

- **[JavaScript Functions Guide](../guides/JavaScript_Functions_Guide.md)** - Functions, callbacks, and scope
- **[JavaScript Objects and Arrays Cheat Sheet](JavaScript_Objects_Arrays_Cheat_Sheet.md)** - Detailed guide on Objects and Arrays
- **[HTML Cheat Sheet](../cheatsheets/HTML_Cheat_Sheet.md)** - Structure of web pages
- **[CSS Cheat Sheet](../cheatsheets/CSS_Cheat_Sheet.md)** - Styling web pages