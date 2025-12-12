# CSS Cheat Sheet

**CSS (Cascading Style Sheets)** describes how HTML elements are to be displayed on screen, paper, or in other media.

---

## 1. Syntax

A CSS rule consists of a selector and a declaration block. The declaration block contains one or more declarations, separated by semicolons. Each declaration includes a CSS property name and a value, separated by a colon.

```css
selector {
    property: value; /* Declaration */
    property: value;
}
```

## 2. Selectors

Selectors are used to "find" (or select) the HTML elements you want to style.

### Basic Selectors

| Selector        | Example      | Description                                      |
| :-------------- | :----------- | :----------------------------------------------- |
| **Element**     | `p`          | Selects all `<p>` elements.                      |
| **ID**          | `#header`    | Selects the element with `id="header"`.          |
| **Class**       | `.btn`       | Selects all elements with `class="btn"`.         |
| **Universal**   | `*`          | Selects all elements.                            |
| **Group**       | `h1, h2`     | Selects all `<h1>` and `<h2>` elements.          |

### Combinator Selectors

| Selector         | Example      | Description                                          |
| :--------------- | :----------- | :--------------------------------------------------- |
| **Descendant**   | `div p`      | Selects all `<p>` elements inside a `<div>`.         |
| **Child**        | `div > p`    | Selects all `<p>` elements that are *direct* children of a `<div>`. |
| **Adjacent Sibling**| `h1 + p`  | Selects the first `<p>` element immediately preceded by an `<h1>`. |
| **General Sibling**| `h1 ~ p`  | Selects all `<p>` elements preceded by an `<h1>`.    |

### Attribute Selectors

Selects elements based on their HTML attributes.

| Selector        | Example             | Description                                          |
| :-------------- | :------------------ | :--------------------------------------------------- |
| `[attr]`        | `[target]`          | Elements with the `target` attribute.                |
| `[attr="value"]`| `[target="_blank"]` | Elements with `target="_blank"`.                    |
| `[attr~="value"]`| `[title~="flower"]` | Elements with `title` containing the word "flower".  |
| `[attr^="value"]`| `[href^="https"]`   | Elements whose `href` attribute value begins with "https". |
| `[attr$="value"]`| `[href$=".pdf"]`    | Elements whose `href` attribute value ends with ".pdf". |
| `[attr*="value"]`| `[title*="test"]`   | Elements whose `title` attribute contains "test".   |

### Pseudo-classes

Used to define a special state of an element.

| Pseudo-class    | Example        | Description                                       |
| :-------------- | :------------- | :------------------------------------------------ |
| `:hover`        | `a:hover`      | Selects an element when the user mouses over it.  |
| `:active`       | `a:active`     | Selects the active link.                          |
| `:focus`        | `input:focus`  | Selects an input element that has focus.          |
| `:visited`      | `a:visited`    | Selects links that have already been visited.     |
| `:link`         | `a:link`       | Selects unvisited links.                          |
| `:first-child`  | `p:first-child`| Selects every `<p>` element that is the first child of its parent. |
| `:last-child`   | `li:last-child`| Selects every `<li>` element that is the last child of its parent. |
| `:nth-child(n)` | `li:nth-child(2n+1)`| Selects every odd `<li>` element.               |
| `:not(selector)`| `p:not(.intro)`| Selects every `<p>` element that does NOT have `class="intro"`. |

```css
/* Example of Pseudo-classes */
a:hover {
    color: blue;
}

input:focus {
    border-color: green;
}

li:first-child {
    font-weight: bold;
}
```

### Pseudo-elements

Used to style a specified part of an element.

| Pseudo-element    | Example            | Description                                  |
| :---------------- | :----------------- | :------------------------------------------- |
| `::before`        | `p::before`        | Inserts something before the content of an element. |
| `::after`         | `p::after`         | Inserts something after the content of an element.  |
| `::first-letter`  | `p::first-letter`  | Selects the first letter of a `<p>` element.  |
| `::first-line`    | `p::first-line`    | Selects the first line of a `<p>` element.    |
| `::selection`     | `::selection`      | Selects the portion of an element that is selected by a user. |
| `::placeholder`   | `input::placeholder`| Selects the placeholder text of an input field. |

```css
/* Example of Pseudo-elements */
h1::before {
    content: "--- ";
    color: grey;
}

p::first-letter {
    font-size: 200%;
    color: #8844AA;
}

input::placeholder {
    color: #ccc;
    font-style: italic;
}
```

## 3. The Box Model

Every HTML element is essentially a box. The CSS box model is a box that wraps around every HTML element. It consists of:
1.  **Content**: The actual content of the element (text, images, video).
2.  **Padding**: Clears an area around the content. It is transparent.
3.  **Border**: A border that goes around the padding and content.
4.  **Margin**: Clears an area outside the border. It is transparent.

```css
.box {
    width: 200px;         /* Content width */
    height: 100px;        /* Content height */
    padding: 20px;        /* Space between content and border */
    border: 5px solid black; /* Border style */
    margin: 10px;         /* Space outside the border */
    box-sizing: border-box; /* Includes padding and border in the element's total width and height */
}
```

## 4. Colors & Backgrounds

```css
body {
    color: #333333; /* Text color (Hexadecimal) */
    background-color: #f4f4f4; /* Background color */
    background-image: url('../images/background.jpg'); /* Background image */
    background-repeat: no-repeat;
    background-size: cover;
}

h1 {
    color: rgb(255, 0, 0);       /* Red (RGB) */
    color: rgba(255, 0, 0, 0.7); /* Red with 70% opacity (RGBA) */
    color: hsl(0, 100%, 50%);    /* Red (HSL) */
}
```

## 5. Text & Fonts

```css
p {
    font-family: "Arial", sans-serif; /* Fallback fonts included */
    font-size: 1rem;                  /* Responsive font size */
    font-weight: 400;                 /* or bold, normal, 700 */
    text-align: center;               /* left, right, justify */
    text-decoration: none;            /* removes underline from links */
    line-height: 1.6;                 /* Spacing between lines of text */
    color: #444;
}

h2 {
    text-transform: uppercase; /* Converts text to uppercase */
    letter-spacing: 2px;       /* Space between characters */
}
```

## 6. Positioning

The `position` property is used to control the exact position of an element on a web page.

*   `static`: (Default) Elements are positioned according to the normal flow of the document. `top`, `right`, `bottom`, `left` properties have no effect.
*   `relative`: The element is positioned relative to its normal position. `top`, `right`, `bottom`, `left` will nudge it from its original spot.
*   `absolute`: The element is positioned relative to its *nearest positioned ancestor* (an ancestor with a position other than `static`). If no such ancestor exists, it's positioned relative to the initial containing block (usually the `<html>` element).
*   `fixed`: The element is positioned relative to the viewport, meaning it always stays in the same place even if the page is scrolled.
*   `sticky`: Toggles between `relative` and `fixed` depending on the scroll position. It's positioned relative until a certain scroll position is met, then it becomes fixed.

```css
.container {
    position: relative; /* Establishes a positioning context for absolute children */
    width: 300px;
    height: 200px;
    border: 1px solid grey;
}

.absolute-box {
    position: absolute;
    top: 20px;
    left: 20px;
    background-color: lightblue;
    padding: 10px;
}

.fixed-header {
    position: fixed;
    top: 0;
    width: 100%;
    background-color: #333;
    color: white;
    text-align: center;
    padding: 10px 0;
    z-index: 1000; /* Controls stacking order */
}
```

## 7. Display Property

The `display` property is one of the most important CSS properties. It controls how an element is rendered on a web page.

*   `block`: The element starts on a new line and takes up the full width available (e.g., `div`, `p`, `h1`).
*   `inline`: The element does not start on a new line and only takes up as much width as necessary (e.g., `span`, `a`, `img`).
*   `inline-block`: Elements are displayed inline but can have `width`, `height`, `margin`, and `padding` applied.
*   `none`: The element is completely removed from the document flow and is not rendered.
*   `flex`: Turns an element into a flex container, enabling Flexbox layout for its direct children.
*   `grid`: Turns an element into a grid container, enabling Grid layout for its direct children.

---

## See Also

-   **[HTML Cheat Sheet](../cheatsheets/HTML_Cheat_Sheet.md)** - HTML5 structure and tags
-   **[CSS Layout Guide](../guides/CSS_Layout_Guide.md)** - In-depth guide to Flexbox and Grid
-   **[JavaScript Basics Cheat Sheet](../cheatsheets/JavaScript_Basics_Cheat_Sheet.md)** - Adding interactivity
-   **[Portfolio Web Development Guide](../guides/Portfolio_Web_Development_Guide.md)** - Practical guide to building a web portfolio