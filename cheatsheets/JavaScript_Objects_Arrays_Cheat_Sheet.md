# JavaScript Objects and Arrays Cheat Sheet

This cheat sheet provides a quick reference for working with objects and arrays in JavaScript, including common operations, methods, and patterns.

---

## Objects

Objects in JavaScript are similar to dictionaries in Python, storing data in key-value pairs.

### Object Creation and Access

```javascript
// Basic Object Creation
const person = {
    name: "Alice",
    age: 30,
    isStudent: false
};

// Accessing values (dot notation)
console.log(person.name); // Output: Alice

// Accessing values (bracket notation - useful for dynamic keys or keys with special characters)
console.log(person["age"]); // Output: 30

// Adding new properties
person.city = "New York";
person["occupation"] = "Engineer";

// Updating properties
person.age = 31;

// Deleting properties
delete person.isStudent;
```

### Object Methods

```javascript
const student = {
    firstName: "John",
    lastName: "Doe",
    age: 20,
    major: "Computer Science",
    greet: function() {
        console.log(`Hello, my name is ${this.firstName} ${this.lastName}`);
    }
};

student.greet(); // Output: Hello, my name is John Doe

// Get all keys
console.log("Keys:", Object.keys(student)); // Output: ["firstName", "lastName", "age", "major", "greet"]

// Get all values
console.log("Values:", Object.values(student)); // Output: ["John", "Doe", 20, "Computer Science", ƒ]

// Get all key-value pairs
console.log("Entries:", Object.entries(student)); // Output: [Array(2), Array(2), Array(2), Array(2), Array(2)]

// Copying objects
const anotherStudent = Object.assign({}, student);
const yetAnotherStudent = { ...student }; // Spread syntax
```

### Iterating Over Objects

```javascript
for (const key in student) {
    if (typeof student[key] !== 'function') { // Exclude functions
        console.log(`${key}: ${student[key]}`);
    }
}

Object.entries(student).forEach(([key, value]) => {
    if (typeof value !== 'function') {
        console.log(`${key}: ${value}`);
    }
});
```

---

## Arrays

Arrays in JavaScript are ordered collections, similar to lists in Python.

### Array Creation and Access

```javascript
// Basic Array Creation
const fruits = ["apple", "banana", "cherry"];

// Accessing elements
console.log(fruits[0]); // Output: apple

// Length of array
console.log(fruits.length); // Output: 3
```

### Adding and Removing Elements (Mutating Methods)

```javascript
const numbers = [1, 2, 3];

// Add to the end
numbers.push(4); // numbers is now [1, 2, 3, 4]
console.log("After push:", numbers);

// Add to the beginning
numbers.unshift(0); // numbers is now [0, 1, 2, 3, 4]
console.log("After unshift:", numbers);

// Remove from the end
const lastItem = numbers.pop(); // lastItem is 4, numbers is [0, 1, 2, 3]
console.log("After pop:", numbers);

// Remove from the beginning
const firstItem = numbers.shift(); // firstItem is 0, numbers is [1, 2, 3]
console.log("After shift:", numbers);

// Splice: Add, remove, or replace elements at any position
// array.splice(startIndex, deleteCount, item1, item2, ...)
let colors = ["red", "green", "blue", "yellow"];
colors.splice(1, 1); // Remove 1 element at index 1 (green) -> ["red", "blue", "yellow"]
console.log("After splice (remove):", colors);

colors.splice(1, 0, "orange", "purple"); // Add at index 1 -> ["red", "orange", "purple", "blue", "yellow"]
console.log("After splice (add):", colors);

colors.splice(3, 1, "cyan"); // Replace 1 element at index 3 (blue) with cyan -> ["red", "orange", "purple", "cyan", "yellow"]
console.log("After splice (replace):", colors);
```

### Non-Mutating Array Methods

```javascript
const originalNumbers = [1, 2, 3, 4, 5];

// Slice: Extracts a section of an array and returns a new array
// array.slice(startIndex, endIndex_exclusive)
const subset = originalNumbers.slice(1, 4); // [2, 3, 4]
console.log("Slice:", subset);
console.log("Original array unchanged:", originalNumbers);

// Concat: Joins two or more arrays
const moreNumbers = [6, 7];
const combined = originalNumbers.concat(moreNumbers); // [1, 2, 3, 4, 5, 6, 7]
console.log("Concat:", combined);

// Join: Joins all elements of an array into a string
const fruitsString = fruits.join(" - "); // "apple - banana - cherry"
console.log("Join:", fruitsString);

// IndexOf, LastIndexOf, Includes
console.log("Index of 'banana':", fruits.indexOf("banana")); // 1
console.log("Includes 'mango':", fruits.includes("mango")); // false
```

### Iterating Over Arrays

```javascript
const scores = [85, 92, 78, 95];

// For...of loop (similar to Python's for...in)
for (const score of scores) {
    console.log(score);
}

// forEach: Executes a provided function once for each array element
scores.forEach((score, index) => {
    console.log(`Score at index ${index}: ${score}`);
});

// map: Creates a new array populated with the results of calling a provided function on every element
let doubledScores = scores.map(score => score * 2); // [170, 184, 156, 190]
console.log("Doubled Scores:", doubledScores);

// filter: Creates a new array with all elements that pass the test implemented by the provided function
let highScores = scores.filter(score => score > 90); // [92, 95]
console.log("High Scores:", highScores);

// find: Returns the first element in the array that satisfies the provided testing function
let firstHighScore = scores.find(score => score > 90); // 92
console.log("First High Score:", firstHighScore);

// reduce: Executes a reducer function on each element of the array, resulting in a single output value
let sumOfScores = scores.reduce((accumulator, currentValue) => accumulator + currentValue, 0); // 350
console.log("Sum of Scores:", sumOfScores);
```

---

## Destructuring

Destructuring assignment syntax is a JavaScript expression that makes it possible to unpack values from arrays, or properties from objects, into distinct variables.

```javascript
// Object Destructuring
const book = {
    title: "The Hitchhiker's Guide to the Galaxy",
    author: "Douglas Adams",
    year: 1979
};

const { title, author } = book;
console.log(title);  // "The Hitchhiker's Guide to the Galaxy"
console.log(author); // "Douglas Adams"

// Array Destructuring
const rgb = [255, 192, 203];
const [red, green, blue] = rgb;
console.log(red, green, blue); // 255 192 203
```

---

## JSON (JavaScript Object Notation)

JSON is a lightweight data-interchange format. It is easy for humans to read and write and for machines to parse and generate.

```javascript
const myObject = { name: "Alice", age: 30 };

// Convert JavaScript object to JSON string
const jsonString = JSON.stringify(myObject);
console.log(jsonString); // '{"name":"Alice","age":30}'

// Convert JSON string back to JavaScript object
const parsedObject = JSON.parse(jsonString);
console.log(parsedObject.name); // 'Alice'
```

---

## Common Patterns and Gotchas

### Object and Array References
Objects and arrays are assigned by reference. Copy them carefully if you need independent copies.

```javascript
const obj1 = { value: 10 };
const obj2 = obj1;
obj2.value = 20;
console.log(obj1.value); // 20 (obj1 was modified)

// Correct way to copy (shallow copy)
const obj3 = { ...obj1 };
obj3.value = 30;
console.log(obj1.value); // 20 (obj1 is unchanged)
```

### Mutating vs. Non-Mutating Methods
Be aware of methods that modify the original array (mutating, e.g., `push`, `pop`, `splice`) versus those that return a new array (non-mutating, e.g., `slice`, `map`, `filter`).

---

## Python vs JavaScript Quick Reference

| Feature         | Python (Dictionaries/Lists)          | JavaScript (Objects/Arrays)              |
| :-------------- | :----------------------------------- | :--------------------------------------- |
| **Object/Dict** | `{key: value}`                       | `{key: value}`                           |
| **Array/List**  | `[item1, item2]`                     | `[item1, item2]`                         |
| **Access**      | `my_dict['key']`, `my_list[0]`       | `myObject.key`, `myArray[0]`             |
| **Add/Update**  | `my_dict['new_key'] = val`           | `myObject.newKey = val`                  |
| **Iterate Keys**| `for key in my_dict:`                | `for (const key in myObject):`           |
| **Iterate Vals**| `for val in my_dict.values():`       | `Object.values(myObject).forEach(val => {})` |
| **Iterate Pairs**| `for k, v in my_dict.items():`      | `Object.entries(myObject).forEach(([k, v]) => {})` |
| **Add to End**  | `my_list.append(item)`               | `myArray.push(item)`                     |
| **Remove from End**| `my_list.pop()`                   | `myArray.pop()`                          |
| **Map/Transform**| `map(func, my_list)`                | `myArray.map(item => {})`                |
| **Filter**      | `filter(func, my_list)`             | `myArray.filter(item => {})`             |