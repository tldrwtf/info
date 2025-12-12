# DOM Manipulation Guide

This guide provides a comprehensive overview of Document Object Model (DOM) manipulation in JavaScript, covering element selection, content and attribute modification, styling, and event handling.

---

## 1. Introduction to the DOM

The Document Object Model (DOM) is a programming interface for web documents. It represents the page structure as a tree of objects, making it possible for programs to alter the document's structure, style, and content.

### Accessing the Document Object
The `document` object is the entry point to the web page's content.

```javascript
// Access the entire document object
console.log(document);

// Access the head and body
console.log(document.head);
console.log(document.body);

// Access the title
console.log(document.title);

// Change the title
document.title = "New Document Title";
```

---

## 2. Element Selection

Selecting elements is the first step in DOM manipulation. JavaScript offers several methods for this.

### Basic Selection Methods

*   **`getElementById('idName')`**: Selects a single element by its unique ID.
*   **`getElementsByClassName('className')`**: Selects all elements with a given class name, returns an HTMLCollection.
*   **`getElementsByTagName('tagName')`**: Selects all elements with a given tag name, returns an HTMLCollection.

```javascript
// Get element by ID
const myHeading = document.getElementById('main-title');
console.log(myHeading);

// Get elements by Class Name
const cards = document.getElementsByClassName('card');
console.log(cards); // Returns an HTMLCollection

// Get elements by Tag Name
const paragraphs = document.getElementsByTagName('p');
console.log(paragraphs); // Returns an HTMLCollection
```

### Modern Selection Methods (`querySelector` & `querySelectorAll`)
These methods use CSS selectors, providing a powerful and flexible way to select elements.

*   **`querySelector('cssSelector')`**: Returns the *first* element that matches the specified CSS selector.
*   **`querySelectorAll('cssSelector')`**: Returns *all* elements that match the specified CSS selector, as a NodeList.

```javascript
// Select by ID (like #id)
const mainTitle = document.querySelector('#main-title');
console.log(mainTitle);

// Select by Class (like .class)
const firstCard = document.querySelector('.card');
console.log(firstCard); // Only the first one

// Select by Tag (like div)
const firstDiv = document.querySelector('div');
console.log(firstDiv);

// Select all elements with class 'card'
const allCards = document.querySelectorAll('.card');
console.log(allCards); // Returns a NodeList

// Select specific elements
const specialListItem = document.querySelector('ul li.special');
console.log(specialListItem);
```

---

## 3. Content Manipulation

Modifying the text or HTML content of elements.

### `textContent`
Gets or sets the text content of a node and its descendants. It strips out HTML tags.

```javascript
const paragraph = document.getElementById('myParagraph');
console.log(paragraph.textContent); // Gets text content

paragraph.textContent = "New text content from JavaScript!"; // Sets text content
```

### `innerHTML`
Gets or sets the HTML or XML markup contained within an element. It parses HTML tags.

```javascript
const contentDiv = document.getElementById('contentArea');
console.log(contentDiv.innerHTML); // Gets HTML content

contentDiv.innerHTML = "<h2>New Heading</h2><p>This is <em>new</em> HTML content.</p>"; // Sets HTML content
```

### `createElement()` and `appendChild()`
Creating new elements and adding them to the DOM.

```javascript
// Create a new div element
const newDiv = document.createElement('div');
newDiv.textContent = "I'm a new div!";
newDiv.classList.add('new-element'); // Add a class

// Append it to the body
document.body.appendChild(newDiv);

// Append it to a specific container
const container = document.getElementById('container');
container.appendChild(newDiv); // Moves the element if it already exists in DOM
```

---

## 4. Attribute Manipulation

Modifying HTML attributes of elements.

### `setAttribute()` and `getAttribute()`
Set or get the value of an attribute.

```javascript
const myImage = document.getElementById('myImage');

// Get attribute
console.log(myImage.getAttribute('src'));

// Set attribute
myImage.setAttribute('alt', 'A beautiful landscape');
myImage.setAttribute('src', 'new_image.jpg');
```

### `classList`
A convenient way to manage an element's class attributes.

*   `add('class')`
*   `remove('class')`
*   `toggle('class')`
*   `contains('class')`

```javascript
const myButton = document.getElementById('toggleButton');

myButton.classList.add('active'); // Add 'active' class
myButton.classList.remove('inactive'); // Remove 'inactive' class

// Toggle 'highlight' class on click
myButton.addEventListener('click', () => {
    myButton.classList.toggle('highlight');
});

if (myButton.classList.contains('active')) {
    console.log("Button is active.");
}
```

---

## 5. Style Manipulation

Changing the CSS styles of elements directly through JavaScript.

### `style` Property
Directly manipulates inline styles.

```javascript
const myElement = document.getElementById('styledElement');

myElement.style.color = 'blue';
myElement.style.backgroundColor = '#f0f0f0';
myElement.style.fontSize = '18px';
// Note: CSS properties like 'background-color' become 'backgroundColor' (camelCase)
```

---

## 6. Event Handling

Responding to user interactions or browser events.

### `addEventListener()`
The preferred method for attaching event handlers.

```javascript
const myBtn = document.getElementById('clickMeBtn');

function handleClick() {
    alert('Button clicked!');
}

// Attach event listener
myBtn.addEventListener('click', handleClick);

// Anonymous function as event handler
myBtn.addEventListener('mouseover', () => {
    console.log('Mouse is over the button!');
});

// Preventing default behavior
const myForm = document.getElementById('myForm');
myForm.addEventListener('submit', (event) => {
    event.preventDefault(); // Prevents the default form submission (page reload)
    alert('Form submitted, but page not reloaded!');
});
```

### Removing Event Listeners
It's good practice to remove event listeners if the element or event handler is no longer needed, especially in single-page applications.

```javascript
myBtn.removeEventListener('click', handleClick);
```

---

## 7. DOM Traversal

Navigating through the DOM tree from one element to another.

*   `parentNode` / `parentElement`
*   `children` (HTMLCollection)
*   `firstChild` / `firstElementChild`
*   `lastChild` / `lastElementChild`
*   `nextSibling` / `nextElementSibling`
*   `previousSibling` / `previousElementSibling`

```javascript
const item = document.getElementById('middle-item');

console.log(item.parentNode);           // Parent node (includes text nodes)
console.log(item.parentElement);        // Parent element (ignores text nodes)
console.log(item.nextElementSibling);   // Next sibling element
console.log(item.previousElementSibling);// Previous sibling element
console.log(item.parentElement.children);// All children elements of the parent
```

---

## See Also

- **[HTML Cheat Sheet](../cheatsheets/HTML_Cheat_Sheet.md)** - Structure of web pages
- **[CSS Cheat Sheet](../cheatsheets/CSS_Cheat_Sheet.md)** - Styling web pages
- **[JavaScript Basics Cheat Sheet](../cheatsheets/JavaScript_Basics_Cheat_Sheet.md)** - Core JavaScript syntax
- **[JavaScript Objects and Arrays Cheat Sheet](../cheatsheets/JavaScript_Objects_Arrays_Cheat_Sheet.md)** - Working with JavaScript data structures
- **[JavaScript Functions Guide](../guides/JavaScript_Functions_Guide.md)** - Deeper dive into functions and scope