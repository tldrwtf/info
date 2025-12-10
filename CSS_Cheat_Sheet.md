# CSS Cheat Sheet

**CSS (Cascading Style Sheets)** describes how HTML elements are to be displayed on screen, paper, or in other media.

## Syntax

```css
selector {
    property: value;
    property: value;
}
```

## Selectors

| Selector | Example | Description |
| :--- | :--- | :--- |
| **Element** | `p` | Selects all `<p>` elements. |
| **ID** | `#header` | Selects the element with `id="header"`. |
| **Class** | `.btn` | Selects all elements with `class="btn"`. |
| **Universal** | `*` | Selects all elements. |
| **Group** | `h1, h2` | Selects all `<h1>` and `<h2>` elements. |
| **Descendant** | `div p` | Selects all `<p>` elements inside a `<div>`. |
| **Child** | `div > p` | Selects all `<p>` elements that are *direct* children of a `<div>`. |
| **Pseudo-class**| `a:hover` | Selects `<a>` links when mouse is over them. |

## The Box Model

Every element in HTML is a box. From inside out:
1.  **Content**: The text or image.
2.  **Padding**: Space between content and border (transparent).
3.  **Border**: Line going around the padding and content.
4.  **Margin**: Space outside the border (separates element from neighbors).

```css
.box {
    width: 200px;
    padding: 20px;
    border: 5px solid black;
    margin: 10px;
}
```

## Colors & Backgrounds

```css
body {
    color: #333333; /* Text color (Hex) */
    background-color: white;
    background-image: url('bg.jpg');
}

h1 {
    color: rgb(255, 0, 0); /* Red */
    color: rgba(255, 0, 0, 0.5); /* 50% opacity red */
}
```

## Text & Fonts

```css
p {
    font-family: "Arial", sans-serif;
    font-size: 16px;
    font-weight: bold; /* or normal, 400, 700 */
    text-align: center; /* left, right, justify */
    text-decoration: none; /* removes underline from links */
    line-height: 1.5;
}
```

## Positioning

*   `static`: Default behavior.
*   `relative`: Positioned relative to its normal position.
*   `absolute`: Positioned relative to the nearest positioned ancestor.
*   `fixed`: Positioned relative to the viewport (stays in place when scrolling).
*   `sticky`: Toggles between relative and fixed depending on scroll position.

```css
.container {
    position: relative;
}

.icon {
    position: absolute;
    top: 10px;
    right: 10px;
}
```

## Display Property

*   `block`: Takes up full width, starts on new line (e.g., `div`, `p`, `h1`).
*   `inline`: Takes up only necessary width, no new line (e.g., `span`, `a`).
*   `inline-block`: Inline flow, but allows width/height/margin/padding.
*   `none`: Hides the element completely.
*   `flex`: Enables Flexbox layout.
*   `grid`: Enables Grid layout.

---

## See Also

- **[HTML Cheat Sheet](./HTML_Cheat_Sheet.md)** - HTML5 structure and tags
- **[CSS Layout Guide](./CSS_Layout_Guide.md)** - In-depth guide to Flexbox and Grid
- **[JavaScript Basics Cheat Sheet](./JavaScript_Basics_Cheat_Sheet.md)** - Adding interactivity