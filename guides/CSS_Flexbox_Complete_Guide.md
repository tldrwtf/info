# CSS Flexbox Complete Guide

## Quick Reference Card

| Property | Values | Purpose |
|---------|--------|---------|
| **display** | `flex` | Enable flexbox on container |
| **flex-direction** | `row`, `row-reverse`, `column`, `column-reverse` | Main axis direction |
| **justify-content** | `start`, `end`, `center`, `space-between`, `space-around`, `space-evenly` | Align on main axis |
| **align-items** | `start`, `end`, `center`, `stretch`, `baseline` | Align on cross axis |
| **flex-wrap** | `nowrap`, `wrap`, `wrap-reverse` | Allow items to wrap |
| **gap** | `20px`, `1rem` | Space between items |
| **flex-grow** | `0`, `1`, `2` | Item growth factor |
| **flex-shrink** | `0`, `1` | Item shrink factor |
| **flex-basis** | `auto`, `200px`, `0` | Item base size |

---

## Table of Contents
1. [What is Flexbox?](#what-is-flexbox)
2. [Flex Direction](#flex-direction)
3. [Justify Content](#justify-content)
4. [Align Items](#align-items)
5. [Flex Wrap](#flex-wrap)
6. [Gap Property](#gap-property)
7. [Positioning vs Flexbox](#positioning-vs-flexbox)
8. [Real-World Patterns](#real-world-patterns)
9. [Flexbox vs Grid](#flexbox-vs-grid)

---

## What is Flexbox?

Flexbox (Flexible Box Layout) is a one-dimensional layout system for arranging items in rows or columns. It excels at distributing space and aligning content within a container.

### Basic Concept

```css
.container {
  display: flex;
}
```

When you set `display: flex` on a container, all direct children become flex items and are automatically arranged in a row.

### Flex Terminology

```
┌──────────────────────────────────────────┐
│  FLEX CONTAINER                          │
│                                          │
│  ┌─────┐  ┌─────┐  ┌─────┐               │
│  │Item │  │Item │  │Item │    ← Flex     │
│  │  1  │  │  2  │  │  3  │      Items    │
│  └─────┘  └─────┘  └─────┘               │
│                                          │
│  ← Main Axis (left to right by default)  │
│                                          │
│  ↑                                       │
│  Cross Axis (top to bottom)              │
└──────────────────────────────────────────┘
```

**Main Axis**: The primary axis along which flex items flow (horizontal by default)
**Cross Axis**: The perpendicular axis (vertical by default)
**justify-content**: Controls alignment on main axis
**align-items**: Controls alignment on cross axis

---

## Flex Direction

The `flex-direction` property defines which direction the main axis runs.

### Row Direction (Default)

```css
main {
  border: 3px solid black;
  height: 50vh;
  padding: 20px;
  background-color: lightgray;
  display: flex;
  flex-direction: row;  /* Default */
}

.box {
  border: 3px solid black;
  width: 100px;
  text-align: center;
  color: rgb(0, 0, 255);
  background-color: rgba(0, 0, 255, 0.246);
}
```

**Result: Items flow left to right**
```
┌────────────────────────────────┐
│  ┌─────┐ ┌─────┐ ┌─────┐       │
│  │Box 1│ │Box 2│ │Box 3│       │
│  └─────┘ └─────┘ └─────┘       │
└────────────────────────────────┘
```

### Row-Reverse

```css
.container {
  display: flex;
  flex-direction: row-reverse;
}
```

**Result: Items flow right to left**
```
┌────────────────────────────────┐
│       ┌─────┐ ┌─────┐ ┌─────┐  │
│       │Box 3│ │Box 2│ │Box 1│  │
│       └─────┘ └─────┘ └─────┘  │
└────────────────────────────────┘
```

### Column Direction

```css
.container-col {
  border: 2px solid black;
  height: 50vh;
  padding: 20px;
  display: flex;
  flex-direction: column;
}
```

**Result: Items flow top to bottom**
```
┌───────────────┐
│  ┌─────────┐  │
│  │  Box 1  │  │
│  └─────────┘  │
│  ┌─────────┐  │
│  │  Box 2  │  │
│  └─────────┘  │
│  ┌─────────┐  │
│  │  Box 3  │  │
│  └─────────┘  │
└───────────────┘
```

### Column-Reverse

```css
.container {
  display: flex;
  flex-direction: column-reverse;
}
```

**Result: Items flow bottom to top**

### When to Use Each Direction

| Direction | Use Case |
|-----------|----------|
| **row** | Navigation bars, horizontal layouts |
| **row-reverse** | RTL languages, reverse ordering |
| **column** | Sidebars, vertical menus, mobile layouts |
| **column-reverse** | Footer content, reversed lists |

---

## Justify Content

The `justify-content` property aligns items along the main axis (horizontal for row, vertical for column).

### All Values Explained

```css
.container {
  display: flex;
  flex-direction: row;
  justify-content: center;  /* Change this value */
}
```

### start (Default)

```css
justify-content: start;
```

**Result: Items packed at the start**
```
┌────────────────────────────────┐
│ ┌───┐ ┌───┐ ┌───┐              │
│ │ 1 │ │ 2 │ │ 3 │              │
│ └───┘ └───┘ └───┘              │
└────────────────────────────────┘
```

### end

```css
justify-content: end;
```

**Result: Items packed at the end**
```
┌────────────────────────────────┐
│             ┌───┐ ┌───┐ ┌───┐  │
│             │ 1 │ │ 2 │ │ 3 │  │
│             └───┘ └───┘ └───┘  │
└────────────────────────────────┘
```

### center

```css
justify-content: center;
```

**Result: Items centered**
```
┌───────────────────────────────┐
│       ┌───┐ ┌───┐ ┌───┐       │
│       │ 1 │ │ 2 │ │ 3 │       │
│       └───┘ └───┘ └───┘       │
└───────────────────────────────┘
```

### space-between

```css
justify-content: space-between;
```

**Result: Even space between items, no space at edges**
```
┌─────────────────────────────┐
│ ┌───┐      ┌───┐      ┌───┐ │
│ │ 1 │      │ 2 │      │ 3 │ │
│ └───┘      └───┘      └───┘ │
└─────────────────────────────┘
```

### space-around

```css
justify-content: space-around;
```

**Result: Equal space around each item**
```
┌───────────────────────────┐
│  ┌───┐    ┌───┐    ┌───┐  │
│  │ 1 │    │ 2 │    │ 3 │  │
│  └───┘    └───┘    └───┘  │
└───────────────────────────┘
```

### space-evenly

```css
justify-content: space-evenly;
```

**Result: Exactly equal space everywhere**
```
┌───────────────────────────┐
│   ┌───┐   ┌───┐   ┌───┐   │
│   │ 1 │   │ 2 │   │ 3 │   │
│   └───┘   └───┘   └───┘   │
└───────────────────────────┘
```

### Real Example: Navigation Bar

```html
<nav>
  <p>Home</p>
  <p>About Us</p>
  <p>Contact</p>
  <p>Schedule</p>
  <p>Login</p>
</nav>
```

```css
nav {
  display: flex;
  height: 6vh;
  justify-content: space-around;  /* Even spacing for nav items */
  align-items: center;
  color: white;
  background-color: rgb(44, 44, 44);
  position: sticky;
  top: 0;
}
```

This creates a navigation bar with evenly spaced menu items.

---

## Align Items

The `align-items` property aligns items along the cross axis (vertical for row, horizontal for column).

### All Values Explained

```css
.container {
  display: flex;
  flex-direction: row;
  height: 50vh;  /* Need height to see vertical alignment */
  align-items: center;  /* Change this value */
}
```

### stretch (Default)

```css
align-items: stretch;
```

**Result: Items stretch to fill container height**
```
┌───────────────────────────┐
│ ┌───────┐ ┌───────┐ ┌───┐ │
│ │       │ │       │ │   │ │
│ │   1   │ │   2   │ │ 3 │ │
│ │       │ │       │ │   │ │
│ └───────┘ └───────┘ └───┘ │
└───────────────────────────┘
```

Items stretch to full height (unless they have a fixed height).

### start

```css
align-items: start;
```

**Result: Items aligned to top**
```
┌───────────────────────────┐
│ ┌───┐ ┌───┐ ┌───┐         │
│ │ 1 │ │ 2 │ │ 3 │         │
│ └───┘ └───┘ └───┘         │
│                           │
│                           │
└───────────────────────────┘
```

### end

```css
align-items: end;
```

**Result: Items aligned to bottom**
```
┌───────────────────────────┐
│                           │
│                           │
│ ┌───┐ ┌───┐ ┌───┐         │
│ │ 1 │ │ 2 │ │ 3 │         │
│ └───┘ └───┘ └───┘         │
└───────────────────────────┘
```

### center

```css
align-items: center;
```

**Result: Items centered vertically**
```
┌───────────────────────────┐
│                           │
│ ┌───┐ ┌───┐ ┌───┐         │
│ │ 1 │ │ 2 │ │ 3 │         │
│ └───┘ └───┘ └───┘         │
│                           │
└───────────────────────────┘
```

This is how you perfectly center items both horizontally and vertically:

```css
.container {
  display: flex;
  justify-content: center;  /* Horizontal centering */
  align-items: center;      /* Vertical centering */
  height: 100vh;
}
```

### baseline

```css
align-items: baseline;
```

**Result: Items aligned by their text baseline**
```
┌──────────────────────────┐
│        ┌────┐            │
│ ┌───┐  │    │  ┌───────┐ │
│ │ 1 │  │ 2  │  │   3   │ │
│ └───┘  │    │  └───────┘ │
│        └────┘            │
└──────────────────────────┘
```

Useful when items have different font sizes but you want text aligned.

---

## Flex Wrap

By default, flex items try to fit on one line. `flex-wrap` controls whether items wrap to new lines.

### nowrap (Default)

```css
.container {
  display: flex;
  flex-wrap: nowrap;  /* Default */
}
```

**Result: All items squeezed onto one line**
```
┌──────────────────────────┐
│ ┌──┐┌──┐┌──┐┌──┐┌──┐┌──┐ │
│ │1 ││2 ││3 ││4 ││5 ││6 │ │
│ └──┘└──┘└──┘└──┘└──┘└──┘ │
└──────────────────────────┘
```

Items may shrink or overflow to fit.

### wrap

```css
main {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  gap: 50px;
}
```

**Result: Items wrap to next line**
```
┌─────────────────────────┐
│ ┌────┐ ┌────┐ ┌────┐    │
│ │ 1  │ │ 2  │ │ 3  │    │
│ └────┘ └────┘ └────┘    │
│                         │
│ ┌────┐ ┌────┐ ┌────┐    │
│ │ 4  │ │ 5  │ │ 6  │    │
│ └────┘ └────┘ └────┘    │
└─────────────────────────┘
```

This is essential for responsive layouts.

### wrap-reverse

```css
.container {
  display: flex;
  flex-wrap: wrap-reverse;
}
```

**Result: Items wrap to lines above instead of below**

### Real Example: Responsive Card Grid

```css
.card-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.card {
  flex-basis: 300px;  /* Preferred width */
  flex-grow: 1;       /* Can grow if space available */
}
```

Cards will wrap to new lines when there's not enough space for 300px cards.

---

## Gap Property

The `gap` property creates space between flex items without using margins.

### Using Gap

```css
main {
  display: flex;
  gap: 50px;  /* Space between all items */
}
```

**Advantages over margin:**
- No extra space at container edges
- Single property for all spacing
- Works with wrap (no double margins)

### Gap vs Margin

```css
/* BAD: Creates unwanted edge spacing */
.box {
  margin: 25px;  /* 50px between items but also at edges */
}

/* GOOD: Space only between items */
.container {
  display: flex;
  gap: 50px;  /* 50px between items, no edge spacing */
}
```

### Separate Row and Column Gap

```css
.container {
  display: flex;
  flex-wrap: wrap;
  row-gap: 30px;     /* Vertical spacing */
  column-gap: 20px;  /* Horizontal spacing */
}

/* Shorthand */
.container {
  gap: 30px 20px;  /* row-gap column-gap */
}
```

---

## Positioning vs Flexbox

CSS positioning and flexbox solve different problems.

### The Five Position Values

```css
/* 1. Static (default) */
.my-static {
  position: static;
  margin-left: 200px;  /* Uses normal flow + margins */
  margin-top: 100px;
}

/* 2. Relative */
.my-relative {
  position: relative;
  left: 200px;  /* Offset from normal position */
  top: 100px;
  background-color: rgba(0, 128, 0, 0.347);
}

/* 3. Absolute */
.my-absolute {
  position: absolute;
  top: 10px;     /* Positioned relative to nearest positioned ancestor */
  left: 20px;
}

/* 4. Fixed */
.my-fixed {
  position: fixed;
  right: 20px;   /* Positioned relative to viewport */
  bottom: 20px;
}

/* 5. Sticky */
.my-sticky {
  position: sticky;
  top: 25px;     /* Sticks when scrolling reaches this point */
}
```

### Real Example: Sticky Navigation

```css
nav {
  display: flex;
  height: 6vh;
  justify-content: space-around;
  align-items: center;
  color: white;
  background-color: rgb(44, 44, 44);
  position: sticky;
  top: 0;
}
```

This creates a navigation bar that:
- Uses flexbox for internal layout
- Sticks to top when scrolling

### Z-Index and Stacking

When elements overlap, `z-index` controls which appears on top.

```css
.back {
  position: relative;
  top: 60px;
  background-color: red;
  z-index: 5;
}

.middle {
  position: relative;
  top: 30px;
  left: 30px;
  background-color: purple;
  z-index: 2;
}

.front {
  position: relative;
  z-index: 9;  /* Highest z-index appears on top */
}
```

**Key Rule:** z-index only works on positioned elements (position: relative, absolute, fixed, or sticky).

### When to Use Each

| Use Case | Solution |
|----------|----------|
| **Layout items in a row/column** | Flexbox |
| **Center content** | Flexbox (justify-content + align-items) |
| **Responsive card grids** | Flexbox with wrap |
| **Navigation bars** | Flexbox |
| **Fixed header/footer** | position: fixed |
| **Sticky navigation** | position: sticky |
| **Overlapping elements** | position: absolute + z-index |
| **Tooltips, modals** | position: absolute or fixed |

---

## Real-World Patterns

### Pattern 1: Centered Hero Section

```html
<div id="hero">
  <h1>Safari</h1>
</div>
```

```css
#hero {
  background-image: url(./safari.jpg);
  height: 20vh;
  background-position: center;
  background-attachment: fixed;
  display: flex;
  justify-content: center;
  align-items: center;
}

h1 {
  color: white;
  font-size: 70px;
}
```

The flexbox properties center the h1 both horizontally and vertically within the hero section.

### Pattern 2: Navigation with Sticky Positioning

```css
nav {
  display: flex;
  height: 6vh;
  justify-content: space-around;
  align-items: center;
  color: white;
  background-color: rgb(44, 44, 44);
  position: sticky;
  top: 0;
}
```

Combines flexbox for layout and sticky positioning to keep nav visible while scrolling.

### Pattern 3: Card Layout

```css
.container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  padding: 20px;
}

.card {
  flex-basis: 250px;
  flex-grow: 1;
  border: 2px solid #ddd;
  border-radius: 8px;
  padding: 20px;
}
```

Cards automatically wrap and grow to fill available space.

### Pattern 4: Flexbox with Grid

```css
.page-layout {
  display: grid;
  grid-template-areas:
    'header header header'
    'sidebar main aside'
    'footer footer footer';
}

header {
  grid-area: header;
  display: flex;           /* Flexbox inside grid item */
  justify-content: space-between;
  align-items: center;
}

nav {
  display: flex;           /* Flexbox for navigation items */
  gap: 30px;
}
```

Use Grid for page layout and Flexbox for components within grid items.

### Pattern 5: Vertical Centering

```css
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background: white;
  padding: 40px;
  border-radius: 8px;
  max-width: 500px;
}
```

Perfect centering of modal dialog on screen.

---

## Flexbox vs Grid

### When to Use Flexbox

Use flexbox for:
- One-dimensional layouts (single row or column)
- Navigation bars
- Centering content
- Space distribution between items
- Components within larger layouts

```css
/* Flexbox: One-dimensional */
.navbar {
  display: flex;
  justify-content: space-between;
}
```

### When to Use Grid

Use grid for:
- Two-dimensional layouts (rows and columns)
- Page layouts
- Complex layouts with overlapping
- Precise item placement
- Gallery layouts

```css
/* Grid: Two-dimensional */
.page-layout {
  display: grid;
  grid-template-columns: 1fr 3fr 1fr;
  grid-template-rows: auto 1fr auto;
}
```

### Combining Both

The most powerful approach is using them together:

```css
/* Grid for page layout */
.page {
  display: grid;
  grid-template-areas:
    'header'
    'main'
    'footer';
}

/* Flexbox for header content */
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* Flexbox for navigation */
nav {
  display: flex;
  gap: 20px;
}

/* Grid for main content cards */
main {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}
```

---

## Summary

**Key Takeaways:**
1. **Flexbox is one-dimensional** - row or column, not both at once
2. **flex-direction** controls main axis (row vs column)
3. **justify-content** aligns on main axis (horizontal for row)
4. **align-items** aligns on cross axis (vertical for row)
5. **flex-wrap** enables multi-line layouts
6. **gap** creates space between items without margin issues
7. **Combine with positioning** for advanced layouts

**Perfect Centering Pattern:**

```css
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
```

**Responsive Card Grid Pattern:**

```css
.card-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.card {
  flex-basis: 300px;
  flex-grow: 1;
}
```

---

## See Also

- [CSS Grid Advanced Guide](./CSS_Grid_Advanced_Guide.md) - Two-dimensional layouts with Grid
- [CSS Cheat Sheet](../cheatsheets/CSS_Cheat_Sheet.md) - Quick CSS reference with positioning, z-index, and alignment
- [CSS Layout Guide](./CSS_Layout_Guide.md) - Comprehensive layout techniques
- [Bootstrap Cheat Sheet](../cheatsheets/Bootstrap_Cheat_Sheet.md) - Bootstrap flexbox utilities
- [React Basics Guide](./React_Basics_Guide.md) - Component layouts with Flexbox
- [Portfolio Web Development Guide](./Portfolio_Web_Development_Guide.md) - Practical layout examples

---
