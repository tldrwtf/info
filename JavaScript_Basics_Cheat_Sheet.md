# JavaScript Basics Cheat Sheet

**JavaScript (JS)** is a lightweight, interpreted programming language with first-class functions. It is best known as the scripting language for Web pages.

## Variables

Modern JavaScript uses `let` and `const`. Avoid `var`.

```javascript
const pi = 3.14;   // Cannot be reassigned
let age = 25;      // Can be reassigned
age = 26;          // OK

// var name = "Bob"; // Legacy (Avoid)
```

## Data Types

| Type | Example | Description |
| :--- | :--- | :--- |
| **String** | `"Hello"`, `'Hi'`, `` `Yo` `` | Text data. |
| **Number** | `42`, `3.14` | Integers and floats are one type. |
| **Boolean** | `true`, `false` | Logical values. |
| **Null** | `null` | Intentional absence of value. |
| **Undefined** | `undefined` | Variable declared but not assigned. |
| **Object** | `{ key: "value" }` | Key-value pairs (like Python dicts). |
| **Array** | `[1, 2, 3]` | Ordered list. |

## Console Output

```javascript
console.log("Hello, World!");
console.error("Something went wrong");
console.warn("Warning!");
```

## Template Literals

Use backticks (`` ` ``) for string interpolation (like Python f-strings).

```javascript
let name = "Alice";
console.log(`Hello, ${name}!`);
```

## Operators

| Operator | Description | Example |
| :--- | :--- | :--- |
| `===` | Strict Equality (Type & Value) | `5 === "5"` is `false` |
| `==` | Loose Equality (Value only) | `5 == "5"` is `true` (Avoid) |
| `!==` | Strict Inequality | `5 !== "5"` is `true` |
| `&&` | Logical AND | `true && false` is `false` |
| `\|\|` | Logical OR | `true \|\| false` is `true` |
| `!` | Logical NOT | `!true` is `false` |

## Conditionals

### If / Else
```javascript
let score = 85;

if (score >= 90) {
    console.log("A");
} else if (score >= 80) {
    console.log("B");
} else {
    console.log("C");
}
```

### Ternary Operator
`condition ? valueIfTrue : valueIfFalse`

```javascript
let age = 20;
let canVote = age >= 18 ? "Yes" : "No";
```

### Switch Statement
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

## Loops

### For Loop (Standard)
```javascript
for (let i = 0; i < 5; i++) {
    console.log(i);
}
```

### For...Of (Arrays)
```javascript
const colors = ["red", "green", "blue"];
for (const color of colors) {
    console.log(color);
}
```

### While Loop
```javascript
let count = 0;
while (count < 3) {
    console.log(count);
    count++;
}
```

## Arrays (Lists)

```javascript
let fruits = ["Apple", "Banana"];

fruits.push("Orange");    // Add to end
fruits.pop();             // Remove from end
fruits.unshift("Grape");  // Add to start
fruits.shift();           // Remove from start

console.log(fruits[0]);   // Access index
console.log(fruits.length); // Length
```

## Objects (Dictionaries)

```javascript
const person = {
    name: "John",
    age: 30,
    isStudent: false
};

console.log(person.name);       // Dot notation (Preferred)
console.log(person["age"]);     // Bracket notation
```

---

## See Also

- **[JavaScript Functions Guide](./JavaScript_Functions_Guide.md)** - Functions, callbacks, and scope
- **[HTML Cheat Sheet](./HTML_Cheat_Sheet.md)** - Structure of web pages
- **[CSS Cheat Sheet](./CSS_Cheat_Sheet.md)** - Styling web pages