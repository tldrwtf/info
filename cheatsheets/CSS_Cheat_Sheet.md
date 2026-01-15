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

The `position` property controls the exact position of an element on a web page. Use `top`, `right`, `bottom`, `left` to adjust position.

### Position Values

| Value      | Behavior | Use Case |
| :--------- | :------- | :------- |
| `static`   | Normal document flow (default) | Most elements |
| `relative` | Relative to its normal position | Small adjustments |
| `absolute` | Relative to nearest positioned ancestor | Tooltips, dropdowns, overlays |
| `fixed`    | Relative to viewport (stays on scroll) | Headers, floating buttons |
| `sticky`   | Relative until scroll threshold, then fixed | Sticky navigation |

**Complete Examples:**

```css
/* 1. Static (default) - no positioning needed */
.normal-element {
    position: static; /* Can be omitted, this is default */
}

/* 2. Relative - nudge from normal position */
.badge {
    position: relative;
    top: -5px; /* Moves up 5px from normal position */
    left: 10px; /* Moves right 10px */
}

/* 3. Absolute - position relative to nearest positioned parent */
.container {
    position: relative; /* Creates positioning context */
    width: 300px;
    height: 200px;
}

.tooltip {
    position: absolute;
    top: 0;    /* 0px from top of .container */
    right: 0;  /* 0px from right of .container */
    background-color: black;
    color: white;
    padding: 5px 10px;
}

/* 4. Fixed - stays in viewport */
.floating-button {
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background-color: #007bff;
}

.fixed-header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background-color: #333;
    color: white;
    z-index: 1000;
}

/* 5. Sticky - relative until scroll threshold */
nav {
    position: sticky;
    top: 0; /* Becomes fixed when scrolled to top */
    background-color: white;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
```

### Z-Index and Stacking Context

The `z-index` property controls the stacking order of overlapping positioned elements. Higher values appear in front of lower values.

**Key Rules:**
- Only works on positioned elements (`position` other than `static`)
- Default z-index is `auto` (same as 0)
- Parent-child relationships affect stacking

**Stacking Order (lowest to highest):**
1. Background and borders of root element
2. Non-positioned elements (in source order)
3. Positioned elements with negative z-index
4. Positioned elements with z-index: auto or 0
5. Positioned elements with positive z-index

```css
/* Example: Modal overlay pattern */
.page-content {
    position: relative;
    z-index: 1; /* Normal content layer */
}

.modal-backdrop {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 1000; /* Above page content */
}

.modal-content {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: white;
    padding: 20px;
    z-index: 1001; /* Above backdrop */
}

.dropdown-menu {
    position: absolute;
    z-index: 100; /* Above normal content, below modals */
}

/* Common z-index scale */
.base-layer { z-index: 1; }
.dropdowns { z-index: 100; }
.sticky-header { z-index: 500; }
.modals { z-index: 1000; }
.tooltips { z-index: 2000; }
```

**Common Pitfall:**
```css
/* BAD: Parent with lower z-index blocks child */
.parent {
    position: relative;
    z-index: 1;
}

.child {
    position: absolute;
    z-index: 9999; /* Still behind elements with z-index: 2 outside parent! */
}

/* GOOD: Keep stacking contexts in mind */
.parent {
    position: relative;
    /* No z-index = doesn't create stacking context */
}

.child {
    position: absolute;
    z-index: 9999; /* Now works as expected */
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

## 8. Alignment Properties Quick Reference

Modern CSS provides powerful alignment properties for Flexbox and Grid layouts. Here's a quick reference for the most common ones.

### Flexbox Alignment

| Property | Applies To | What It Controls | Common Values |
| :------- | :--------- | :--------------- | :------------ |
| `justify-content` | Flex container | Main axis alignment (horizontal for row) | `flex-start`, `center`, `flex-end`, `space-between`, `space-around`, `space-evenly` |
| `align-items` | Flex container | Cross axis alignment (vertical for row) | `stretch`, `flex-start`, `center`, `flex-end`, `baseline` |
| `align-self` | Flex item | Override align-items for single item | Same as `align-items` |
| `flex-direction` | Flex container | Main axis direction | `row`, `row-reverse`, `column`, `column-reverse` |
| `gap` | Flex container | Space between items | Any length value (e.g., `10px`, `1rem`) |

**Common Flexbox Patterns:**

```css
/* Perfect centering */
.center-box {
    display: flex;
    justify-content: center; /* Horizontal center */
    align-items: center;     /* Vertical center */
    height: 100vh;
}

/* Space between items */
.navbar {
    display: flex;
    justify-content: space-between; /* Items at edges, space in middle */
    align-items: center;
}

/* Column layout */
.sidebar {
    display: flex;
    flex-direction: column;
    gap: 20px; /* Space between items */
}
```

### Grid Alignment

| Property | Applies To | What It Controls | Common Values |
| :------- | :--------- | :--------------- | :------------ |
| `justify-items` | Grid container | Horizontal alignment of items within their cells | `start`, `center`, `end`, `stretch` |
| `align-items` | Grid container | Vertical alignment of items within their cells | `start`, `center`, `end`, `stretch` |
| `justify-content` | Grid container | Horizontal alignment of entire grid | `start`, `center`, `end`, `space-between`, `space-around`, `space-evenly` |
| `align-content` | Grid container | Vertical alignment of entire grid | `start`, `center`, `end`, `space-between`, `space-around`, `space-evenly` |
| `justify-self` | Grid item | Override justify-items for single item | Same as `justify-items` |
| `align-self` | Grid item | Override align-items for single item | Same as `align-items` |
| `gap` | Grid container | Space between grid cells | Any length value or two values for row/column gap |

**Common Grid Patterns:**

```css
/* Centered grid items */
.grid-gallery {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    justify-items: center; /* Center items horizontally in cells */
    align-items: center;   /* Center items vertically in cells */
}

/* Center entire grid on page */
.container {
    display: grid;
    grid-template-columns: 300px 300px;
    justify-content: center; /* Center the grid horizontally */
    align-content: center;   /* Center the grid vertically */
    height: 100vh;
    gap: 10px;
}
```

**Key Differences:**

- **Flexbox** is one-dimensional (row OR column). `justify-content` controls the main axis, `align-items` controls the cross axis.
- **Grid** is two-dimensional (rows AND columns). `justify-*` always controls horizontal, `align-*` always controls vertical.
- For detailed examples and responsive layouts, see the dedicated guides below.

---

## See Also

- [HTML Cheat Sheet](HTML_Cheat_Sheet.md) - HTML5 structure and semantic tags
- [CSS Layout Guide](../guides/CSS_Layout_Guide.md) - In-depth guide to Flexbox and Grid
- [CSS Flexbox Complete Guide](../guides/CSS_Flexbox_Complete_Guide.md) - Complete flexbox patterns and real-world examples
- [CSS Grid Advanced Guide](../guides/CSS_Grid_Advanced_Guide.md) - Advanced grid layouts with template areas
- [Bootstrap Cheat Sheet](Bootstrap_Cheat_Sheet.md) - CSS framework with pre-built components
- [JavaScript Basics Cheat Sheet](JavaScript_Basics_Cheat_Sheet.md) - Adding interactivity
- [Portfolio Web Development Guide](../guides/Portfolio_Web_Development_Guide.md) - Practical guide to building a web portfolio