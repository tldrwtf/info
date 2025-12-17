# JavaScript Workshops: Practical Code Scenarios

This guide provides a collection of hands-on code scenarios and "mini-projects" that demonstrate core JavaScript concepts in action. Each example is heavily commented to explain the *why* and *how* behind the code.

## Table of Contents
1. [Logic & Control Flow: Season Determiner](#1-logic--control-flow-season-determiner)
2. [Array Manipulation: Shopping Cart Logic](#2-array-manipulation-shopping-cart-logic)
3. [DOM Interaction: Interactive Color Picker](#3-dom-interaction-interactive-color-picker)
4. [Data Persistence: Local Storage Form](#4-data-persistence-local-storage-form)
5. [Event Delegation: Dynamic List Management](#5-event-delegation-dynamic-list-management)

---

## 1. Logic & Control Flow: Season Determiner

**Concepts:** Functions, `if/else if/else`, Logical Operators (`&&`), Return values.

This function determines the season based on a given month number (1-12).

```javascript
/**
 * Determines the season based on the month number.
 * 
 * @param {number} month - The month number (1 for January, 12 for December).
 * @returns {string} - The name of the season ("Spring", "Summer", "Fall", "Winter") or "Invalid Month".
 */
function getSeason(month) {
    // Check if the month is valid (must be between 1 and 12)
    if (month < 1 || month > 12) {
        return "Invalid Month";
    }

    // Spring: March (3), April (4), May (5)
    // We use the AND operator (&&) to check ranges.
    if (month >= 3 && month <= 5) {
        return "Spring";
    } 
    // Summer: June (6), July (7), August (8)
    else if (month >= 6 && month <= 8) {
        return "Summer";
    } 
    // Fall: September (9), October (10), November (11)
    else if (month >= 9 && month <= 11) {
        return "Fall";
    } 
    // Winter: December (12), January (1), February (2)
    // This is the "catch-all" else because we already validated 1-12 at the start.
    else {
        return "Winter";
    }
}

// === Testing the Function ===
console.log(getSeason(4));  // Output: Spring
console.log(getSeason(8));  // Output: Summer
console.log(getSeason(1));  // Output: Winter
console.log(getSeason(13)); // Output: Invalid Month
```

---

## 2. Array Manipulation: Shopping Cart Logic

**Concepts:** Objects, Arrays, `this` keyword, Array Methods (`push`, `find`, `findIndex`, `splice`, `reduce`).

A simplified shopping cart object that manages items, prices, and quantities.

```javascript
const shoppingCart = {
    // The cart's storage: an array of item objects
    items: [],

    /**
     * Adds an item to the cart. If the item exists, increases quantity.
     * @param {string} name - Name of the product
     * @param {number} price - Price per unit
     * @param {number} quantity - Quantity to add
     */
    addItem: function(name, price, quantity) {
        // 1. Check if item already exists in the array
        // .find() returns the *first* element that matches the condition, or undefined.
        const existingItem = this.items.find(item => item.name === name);

        if (existingItem) {
            // Logic: If item exists, just update the quantity property.
            console.log(`Updating quantity for ${name}...`);
            existingItem.quantity += quantity;
        } else {
            // Logic: If it's new, create a new object and push it to the array.
            console.log(`Adding new item: ${name}...`);
            const newItem = {
                name: name,
                price: price,
                quantity: quantity
            };
            this.items.push(newItem);
        }
    },

    /**
     * Removes an item completely from the cart by name.
     * @param {string} name - Name of the product to remove
     */
    removeItem: function(name) {
        // 1. Find the index of the item
        // .findIndex() returns the index (0, 1, 2...) or -1 if not found.
        const index = this.items.findIndex(item => item.name === name);

        if (index !== -1) {
            // 2. Use .splice() to modify the array in place.
            // splice(startIndex, deleteCount)
            this.items.splice(index, 1);
            console.log(`${name} removed from cart.`);
        } else {
            console.log(`${name} not found in cart.`);
        }
    },

    /**
     * Calculates the total cost of all items.
     * @returns {number} - Total cost
     */
    calculateTotal: function() {
        // .reduce() accumulates a value by iterating over the array.
        // acc: accumulator (running total)
        // item: current item in the loop
        // 0: initial value of the accumulator
        return this.items.reduce((acc, item) => {
            return acc + (item.price * item.quantity);
        }, 0);
    }
};

// === Testing the Cart ===
shoppingCart.addItem("Apple", 1.50, 2);  // Add 2 Apples
shoppingCart.addItem("Banana", 0.80, 5); // Add 5 Bananas
shoppingCart.addItem("Apple", 1.50, 3);  // Add 3 more Apples (Total 5)

console.log("Current Cart:", shoppingCart.items);
// Output: [{name: "Apple", price: 1.5, quantity: 5}, {name: "Banana", ...}]

console.log("Total Cost: $" + shoppingCart.calculateTotal()); 
// (5 * 1.50) + (5 * 0.80) = 7.50 + 4.00 = 11.50

shoppingCart.removeItem("Banana");
console.log("Cart after removing Banana:", shoppingCart.items);
```

---

## 3. DOM Interaction: Interactive Color Picker

**Concepts:** DOM Selection (`querySelectorAll`, `getElementById`), Event Listeners (`click`), Style Manipulation, `dataset` attributes.

**HTML Structure (assumed):**
```html
<div class="swatch" data-color="red" style="background-color: red;"></div>
<div class="swatch" data-color="blue" style="background-color: blue;"></div>
<div id="canvas" style="width: 200px; height: 200px; border: 1px solid black;"></div>
```

**JavaScript Implementation:**

```javascript
// 1. Select all elements with the class 'swatch'
// querySelectorAll returns a NodeList (similar to an array)
const swatches = document.querySelectorAll(".swatch");

// 2. Select the target element we want to change
const canvas = document.getElementById("canvas");

/**
 * Helper function to handle the color change logic.
 * @param {string} color - The color string (e.g., "red", "#ff0000")
 */
const updateCanvasColor = (color) => {
    console.log(`Changing background to: ${color}`);
    canvas.style.backgroundColor = color;
    
    // Optional: Add a text indicator
    canvas.textContent = `Current Color: ${color}`;
    canvas.style.color = "white"; // Ensure text is visible
    canvas.style.display = "flex";
    canvas.style.justifyContent = "center";
    canvas.style.alignItems = "center";
};

// 3. Loop through each swatch to attach an event listener
swatches.forEach(swatch => {
    swatch.addEventListener("click", (event) => {
        // 'event.target' refers to the specific element that was clicked
        
        // Access custom data attributes using .dataset
        // HTML: data-color="red" -> JS: dataset.color
        const selectedColor = event.target.dataset.color;
        
        // Call our helper function
        updateCanvasColor(selectedColor);
    });
});
```

---

## 4. Data Persistence: Local Storage Form

**Concepts:** `localStorage` API (`setItem`, `getItem`), JSON serialization (`JSON.stringify`, `JSON.parse`), Form Events (`submit`), Preventing default browser behavior.

**HTML Structure (assumed):**
```html
<form id="preferences-form">
    <input type="text" id="username" placeholder="Enter username" />
    <select id="theme">
        <option value="light">Light Mode</option>
        <option value="dark">Dark Mode</option>
    </select>
    <button type="submit">Save Preferences</button>
</form>
```

**JavaScript Implementation:**

```javascript
const form = document.getElementById("preferences-form");
const usernameInput = document.getElementById("username");
const themeInput = document.getElementById("theme");

// 1. Function to load saved data when the page opens
const loadPreferences = () => {
    // Retrieve string data from Local Storage
    const savedData = localStorage.getItem("userPreferences");

    if (savedData) {
        // Convert string back into a JavaScript Object
        const preferences = JSON.parse(savedData);
        
        // Pre-fill form inputs
        usernameInput.value = preferences.username;
        themeInput.value = preferences.theme;
        
        console.log("Preferences loaded:", preferences);
        
        // Optional: Apply theme immediately
        document.body.className = preferences.theme; 
    }
};

// 2. Event Listener for Form Submission
form.addEventListener("submit", (event) => {
    // CRITICAL: Prevent the browser from refreshing the page
    event.preventDefault();

    // Create an object with the current form values
    const preferences = {
        username: usernameInput.value,
        theme: themeInput.value
    };

    // Save to Local Storage
    // Local Storage ONLY stores strings, so we must use JSON.stringify()
    localStorage.setItem("userPreferences", JSON.stringify(preferences));

    console.log("Preferences saved!", preferences);
    alert("Settings saved successfully.");
});

// 3. Run load function immediately when script runs (page load)
loadPreferences();
```

---

## 5. Event Delegation: Dynamic List Management

**Concepts:** Event Delegation (listening on parent), Event Bubbling, Dynamic Element Creation.

**Scenario:** A To-Do list where items can be added dynamically. We want to click a "Delete" button on any item, even ones created *after* the page loaded.

**HTML Structure (assumed):**
```html
<ul id="todo-list">
    <li>Buy Milk <button class="delete-btn">X</button></li>
</ul>
<button id="add-btn">Add Task</button>
```

**JavaScript Implementation:**

```javascript
const todoList = document.getElementById("todo-list");
const addBtn = document.getElementById("add-btn");

// 1. Add Event Listener to the PARENT (<ul>), not individual items.
// This is "Event Delegation". The event "bubbles up" from the button to the ul.
todoList.addEventListener("click", (event) => {
    // Check WHAT was clicked inside the list
    const clickedElement = event.target;

    // We only care if the clicked element has the class 'delete-btn'
    if (clickedElement.classList.contains("delete-btn")) {
        // Find the parent <li> of the clicked button
        const listItem = clickedElement.parentElement;
        
        // Remove the <li> from the DOM
        listItem.remove();
        console.log("Task removed!");
    }
});

// 2. Logic to add new items (to demonstrate delegation works on new items)
addBtn.addEventListener("click", () => {
    const newItem = document.createElement("li");
    newItem.innerHTML = `New Task ${Date.now()} <button class="delete-btn">X</button>`;
    
    // Append to the list
    todoList.appendChild(newItem);
    console.log("New task added.");
    // Notice we did NOT add a click listener to the new button.
    // The parent <ul> listener handles it automatically!
});
```

---

## See Also

- **[JavaScript Basics Cheat Sheet](../cheatsheets/JavaScript_Basics_Cheat_Sheet.md)**
- **[JavaScript Objects and Arrays Cheat Sheet](../cheatsheets/JavaScript_Objects_Arrays_Cheat_Sheet.md)**
- **[DOM Manipulation Guide](DOM_Manipulation_Guide.md)**
