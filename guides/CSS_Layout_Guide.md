# CSS Layout Guide: Flexbox & Grid

Modern CSS layouts rely heavily on **Flexbox** (for one-dimensional alignment) and **Grid** (for two-dimensional control). This guide explores their core concepts, properties, and practical applications, including integration with Bootstrap's grid system.

---

## 1. Flexbox (One-Dimensional Layout)

Flexbox is a powerful one-dimensional layout system that allows you to design a flexible responsive layout structure without using float or positioning. It's ideal for distributing space among items in a single row or column.

### Flex Container Properties (`display: flex`)

These properties are applied to the parent element (the flex container).

| Property           | Values                                                                | Description                                                                                             |
| :----------------- | :-------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------ |
| `flex-direction`   | `row` (default), `column`, `row-reverse`, `column-reverse`          | Defines the primary axis along which flex items are laid out.                                         |
| `justify-content`  | `flex-start`, `flex-end`, `center`, `space-between`, `space-around`, `space-evenly` | Aligns flex items along the **main axis** (horizontal if `flex-direction: row`). Controls spacing between items. |
| `align-items`      | `stretch` (default), `flex-start`, `flex-end`, `center`, `baseline` | Aligns flex items along the **cross axis** (vertical if `flex-direction: row`).                         |
| `flex-wrap`        | `nowrap` (default), `wrap`, `wrap-reverse`                          | Controls whether flex items are forced onto a single line or can wrap onto multiple lines.             |
| `align-content`    | `stretch`, `flex-start`, `flex-end`, `center`, `space-between`, `space-around` | Aligns flex *lines* when there is extra space in the cross-axis and `flex-wrap` is set to `wrap`.       |

**Flexbox Example (`flex.html`, `styles.css`):**

```html
<!-- flex.html snippet -->
<div class="flex-container">
    <div class="flex-item">1</div>
    <div class="flex-item">2</div>
    <div class="flex-item">3</div>
</div>
```

```css
/* styles.css snippet for Flexbox */
.flex-container {
    display: flex;
    flex-direction: row; /* Default */
    justify-content: space-around; /* Distribute items with space around them */
    align-items: center; /* Vertically center items */
    flex-wrap: wrap; /* Allow items to wrap to the next line */
    height: 200px;
    background-color: #f0f0f0;
    border: 1px solid #ccc;
}

.flex-item {
    background-color: #3498db;
    color: white;
    padding: 20px;
    margin: 10px;
    width: 80px; /* Example fixed width */
    text-align: center;
}
```

### Flex Item Properties

These properties are applied to the child elements (the flex items).

| Property      | Values                                | Description                                                 |
| :------------ | :------------------------------------ | :---------------------------------------------------------- |
| `flex-grow`   | `number` (default `0`)                | Defines the ability for a flex item to grow if necessary.   |
| `flex-shrink` | `number` (default `1`)                | Defines the ability for a flex item to shrink if necessary. |
| `flex-basis`  | `length` (e.g., `20%`, `auto`, `300px`)| Defines the default size of an element before the remaining space is distributed. |
| `flex`        | `flex-grow flex-shrink flex-basis`    | Shorthand for `flex-grow`, `flex-shrink`, and `flex-basis`. Common values are `1 1 auto` or `0 0 auto`. |
| `order`       | `integer` (default `0`)               | Controls the order in which flex items appear in the flex container. |
| `align-self`  | `auto`, `flex-start`, `flex-end`, `center`, `baseline`, `stretch` | Overrides the `align-items` property for a single flex item. |

---

## 2. CSS Grid (Two-Dimensional Layout)

CSS Grid Layout is a two-dimensional layout system for the web. It lets you lay out content in rows and columns, offering precise control over the design.

### Grid Container Properties (`display: grid`)

These properties are applied to the parent element (the grid container).

| Property                 | Values                                                                     | Description                                                                                               |
| :----------------------- | :------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------- |
| `grid-template-columns`  | `1fr 1fr 1fr`, `200px auto`, `repeat(3, 1fr)`                            | Defines the columns of the grid with a space-separated list of values. `fr` is a fractional unit.         |
| `grid-template-rows`     | `100px auto 50px`, `repeat(2, 100px)`                                    | Defines the rows of the grid with a space-separated list of values.                                       |
| `gap` (or `grid-gap`)    | `10px`, `1rem`, `row-gap: 10px; column-gap: 20px;`                       | Sets the size of the gaps (gutters) between the rows and columns.                                         |
| `grid-template-areas`    | `header header` `sidebar main`                                           | Defines named grid areas to make grid layouts easier to understand and manage.                          |
| `justify-items`          | `start`, `end`, `center`, `stretch`                                      | Aligns grid items along the **inline (row) axis** within their grid area.                                |
| `align-items`            | `start`, `end`, `center`, `stretch`                                      | Aligns grid items along the **block (column) axis** within their grid area.                              |
| `justify-content`        | `start`, `end`, `center`, `space-between`, `space-around`, `space-evenly`| Aligns the **grid itself** inside the grid container along the inline axis when the total size of grid is less than the container. |
| `align-content`          | `start`, `end`, `center`, `space-between`, `space-around`, `space-evenly`| Aligns the **grid itself** inside the grid container along the block axis when the total size of grid is less than the container. |

**CSS Grid Example (`grid_layout/index.html`, `grid_layout/style.css`):**

```html
<!-- grid_layout/index.html snippet -->
<div class="grid-container">
    <div class="header">Header</div>
    <div class="sidebar">Sidebar</div>
    <div class="main">Main Content</div>
    <div class="footer">Footer</div>
</div>
```

```css
/* grid_layout/style.css snippet */
.grid-container {
    display: grid;
    grid-template-columns: 1fr 3fr 1fr; /* Three columns: flexible, larger flexible, flexible */
    grid-template-rows: auto 1fr auto; /* Header, flexible main content, footer */
    gap: 15px;
    height: 100vh;
    background-color: #eee;
}

.header {
    grid-column: 1 / -1; /* Span across all columns */
    background-color: #e74c3c;
    padding: 20px;
    text-align: center;
}

.sidebar {
    background-color: #3498db;
    padding: 20px;
}

.main {
    background-color: #2ecc71;
    padding: 20px;
}

.footer {
    grid-column: 1 / -1; /* Span across all columns */
    background-color: #9b59b6;
    padding: 20px;
    text-align: center;
}
```

### Grid Item Properties

These properties are applied to the child elements (the grid items).

| Property         | Values                                  | Description                                                           |
| :--------------- | :-------------------------------------- | :-------------------------------------------------------------------- |
| `grid-column-start` / `grid-column-end` | `line-number`, `span n`, `name` | Specifies a grid item's start/end position within the column tracks.  |
| `grid-row-start` / `grid-row-end`    | `line-number`, `span n`, `name` | Specifies a grid item's start/end position within the row tracks.     |
| `grid-column`    | `start / end`                           | Shorthand for `grid-column-start` and `grid-column-end`.            |
| `grid-row`       | `start / end`                           | Shorthand for `grid-row-start` and `grid-row-end`.                  |
| `grid-area`      | `name` (from `grid-template-areas`)   | Assigns a name to a grid item so it can be referenced by the `grid-template-areas` property. |
| `justify-self`   | `start`, `end`, `center`, `stretch`   | Aligns a single grid item inside its grid cell along the inline (row) axis. |
| `align-self`     | `start`, `end`, `center`, `stretch`   | Aligns a single grid item inside its grid cell along the block (column) axis. |

---

## 3. Bootstrap Grid System

Bootstrap's grid system is built with Flexbox and provides a responsive, mobile-first fluid grid system that appropriately scales up to 12 columns as the device or viewport size increases.

### Key Concepts

*   **Containers (`.container`, `.container-fluid`):** Provide a responsive fixed-width container or a full-width container for your content.
*   **Rows (`.row`):** Horizontal groups of columns. Rows must be placed within a `.container` (fixed-width) or `.container-fluid` (full-width) for proper alignment and padding.
*   **Columns (`.col-*`):** Specify the number of columns to span across. Bootstrap uses a 12-column system.
    *   `col-sm-`, `col-md-`, `col-lg-`, `col-xl-`: Define column behavior at different breakpoints (small, medium, large, extra-large devices).
*   **Breakpoints:** Bootstrap has 5 default responsive breakpoints, from `xs` (extra small, not explicitly in class name) to `xxl`.

**Bootstrap Grid Example (`bootstrap_demo/index.html`):**

```html
<!-- bootstrap_demo/index.html snippet -->
<div class="container">
    <div class="row">
        <div class="col-md-6 col-lg-4">
            <div class="card">
                <h3>Column 1</h3>
                <p>This column takes 6 units on medium screens, and 4 on large screens.</p>
            </div>
        </div>
        <div class="col-md-6 col-lg-4">
            <div class="card">
                <h3>Column 2</h3>
                <p>Another column with responsive sizing.</p>
            </div>
        </div>
        <div class="col-md-12 col-lg-4">
            <div class="card">
                <h3>Column 3</h3>
                <p>This column takes full width on medium, and 4 on large screens.</p>
            </div>
        </div>
    </div>
</div>
```

### Offset & Ordering

*   **Offsetting columns:** Use `.offset-md-*` classes to move columns to the right.
*   **Reordering columns:** Use `.order-*` classes to visually reorder columns.

---

## 4. Positioning (When to use it)

While Flexbox and Grid manage the overall layout, CSS positioning is still essential for specific use cases like overlays, sticky headers, and fine-tuning element placement.

*   **`static`**: The default value. Elements render in order as they appear in the document flow. `top`, `right`, `bottom`, `left` properties have no effect.
*   **`relative`**: The element is positioned relative to its normal position. Setting `top`, `right`, `bottom`, and `left` properties will nudge the element from its original position without affecting the layout of other elements.
*   **`absolute`**: The element is removed from the normal document flow and is positioned relative to its *nearest positioned ancestor*. If no such ancestor exists, it is positioned relative to the initial containing block (usually the `<html>` element).
*   **`fixed`**: The element is removed from the normal document flow and is positioned relative to the viewport. It remains in the same position even when the page is scrolled. Useful for sticky headers or "back to top" buttons.
*   **`sticky`**: The element is positioned based on the user's scroll position. It acts like `relative` until a certain scroll threshold is met, after which it becomes `fixed` to its position.

**Positioning Example (`z-index.html`):**

```html
<!-- z-index.html snippet -->
<div class="container-relative">
    <div class="box absolute-box-1">Box 1</div>
    <div class="box absolute-box-2">Box 2</div>
</div>
```

```css
/* styles.css snippet for Positioning */
.container-relative {
    position: relative; /* Establishes a positioning context */
    width: 300px;
    height: 200px;
    border: 2px solid #e74c3c;
    margin-bottom: 30px;
}

.box {
    width: 100px;
    height: 100px;
    background-color: #3498db;
    color: white;
    text-align: center;
    line-height: 100px;
    position: absolute; /* Allows precise positioning within container */
}

.absolute-box-1 {
    top: 10px;
    left: 10px;
    z-index: 2; /* Controls stacking order */
}

.absolute-box-2 {
    top: 30px;
    left: 30px;
    background-color: #2ecc71;
    z-index: 1;
}

.fixed-element {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background-color: #9b59b6;
    color: white;
    padding: 10px 15px;
    border-radius: 5px;
}
```

---

## 5. Responsive Design with Media Queries

While frameworks like Bootstrap handle responsiveness for you, understanding **Media Queries** is essential for custom CSS layouts. They allow you to apply CSS rules only when specific conditions (like viewport width) are met.

### Basic Syntax

```css
@media (min-width: 768px) {
    /* Rules here apply only if the screen is 768px or wider */
    .container {
        width: 750px;
    }
}
```

### Common Breakpoints
These often align with device sizes (Phones, Tablets, Desktops).

*   **Mobile First (Default):** `< 576px`
*   **Small (Landscape Phones):** `≥ 576px`
*   **Medium (Tablets):** `≥ 768px`
*   **Large (Desktops):** `≥ 992px`
*   **Extra Large:** `≥ 1200px`

### Example: Responsive Flexbox

Changing a layout from a vertical column (mobile) to a horizontal row (desktop).

```css
/* Default (Mobile) - Stacked vertically */
.nav-menu {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

/* Tablet and up - Horizontal row */
@media (min-width: 768px) {
    .nav-menu {
        flex-direction: row;
        justify-content: space-between;
    }
}
```

---

## See Also

- [CSS Cheat Sheet](../cheatsheets/CSS_Cheat_Sheet.md) - Basic CSS properties and selectors
- [CSS Flexbox Complete Guide](CSS_Flexbox_Complete_Guide.md) - Complete flexbox patterns with detailed examples
- [CSS Grid Advanced Guide](CSS_Grid_Advanced_Guide.md) - Advanced grid layouts with template areas
- [HTML Cheat Sheet](../cheatsheets/HTML_Cheat_Sheet.md) - HTML structure and tags
- [Bootstrap Cheat Sheet](../cheatsheets/Bootstrap_Cheat_Sheet.md) - Pre-built layout components with Bootstrap
- [Portfolio Web Development Guide](Portfolio_Web_Development_Guide.md) - Practical guide to building a web portfolio
- [DOM Manipulation Guide](DOM_Manipulation_Guide.md) - Learn how to interact with HTML elements using JavaScript