# CSS Grid Advanced Guide

## Quick Reference Card

| Property | Syntax | Purpose |
|---------|--------|---------|
| **Grid Template Areas** | `grid-template-areas: 'header header'` | Named grid regions |
| **Grid Area** | `grid-area: header` | Assign element to named area |
| **Grid Column** | `grid-column: 1 / 4` | Span columns by line numbers |
| **Grid Column Span** | `grid-column: span 2` | Span multiple columns |
| **Grid Row** | `grid-row: 2 / 4` | Span rows by line numbers |
| **Grid Row Span** | `grid-row: span 2` | Span multiple rows |
| **Fr Units** | `grid-template-columns: 1fr 2fr` | Flexible fractional units |
| **Repeat** | `repeat(3, 1fr)` | Repeat column/row definitions |
| **Gap** | `gap: 20px` | Space between grid items |
| **Auto-fill** | `repeat(auto-fill, minmax(200px, 1fr))` | Responsive columns |

---

## Table of Contents
1. [What is Grid Template Areas?](#what-is-grid-template-areas)
2. [Grid Item Placement](#grid-item-placement)
3. [Building Real Layouts](#building-real-layouts)
4. [Responsive Grid Reconfiguration](#responsive-grid-reconfiguration)
5. [Gallery Pattern](#gallery-pattern)
6. [Advanced Techniques](#advanced-techniques)
7. [Common Patterns](#common-patterns)

---

## What is Grid Template Areas?

Grid template areas let you create layouts using named regions. Think of it as drawing a blueprint of your layout with words instead of numbers.

### The Basic Concept

```css
.grid-container {
  display: grid;
  grid-template-columns: 0.5fr 2fr 0.5fr;
  grid-template-rows: 1fr 5fr 1fr;
  height: 100vh;
  grid-template-areas:
    'header header header'
    'left-aside main right-aside'
    'footer footer footer';
}

header {
  grid-area: header;
}

.left-aside {
  grid-area: left-aside;
}

main {
  grid-area: main;
}

.right-aside {
  grid-area: right-aside;
}

footer {
  grid-area: footer;
}
```

This creates a classic web layout with header, two sidebars, main content, and footer. The beauty is that you can see the layout structure just by looking at the grid-template-areas definition.

### Visual Layout Blueprint

```
┌─────────────────────────────────┐
│           HEADER                │
├──────────┬──────────────┬───────┤
│  LEFT    │              │ RIGHT │
│  ASIDE   │     MAIN     │ ASIDE │
│          │              │       │
├──────────┴──────────────┴───────┤
│           FOOTER                │
└─────────────────────────────────┘
```

The grid-template-areas property literally mirrors this visual structure:
```css
grid-template-areas:
  'header header header'
  'left-aside main right-aside'
  'footer footer footer';
```

### Why Use Template Areas?

**Advantages:**
- **Visual clarity** - You can see the layout in your CSS
- **Semantic naming** - Use meaningful names instead of numbers
- **Easy responsive changes** - Redefine areas for different screen sizes
- **No math required** - No calculating column spans

**Example HTML:**
```html
<div class="grid-container">
  <header>Logo and Navigation</header>
  <aside class="left-aside">Sidebar</aside>
  <main>Main Content</main>
  <aside class="right-aside">Widgets</aside>
  <footer>Copyright Info</footer>
</div>
```

---

## Grid Item Placement

There are three main ways to position grid items. Each has its use case.

### Method 1: Grid Column/Row with Line Numbers

```css
.grid-container {
  display: grid;
  grid-template-columns: 0.5fr 2fr 0.5fr;
  grid-template-rows: 1fr 5fr 1fr;
  height: 100vh;
}

header {
  border: 3px solid black;
  grid-column: 1/4;  /* Start at line 1, end at line 4 (spans all columns) */
}

aside {
  border: 3px solid red;
}

main {
  border: 3px solid green;
}

footer {
  border: 3px solid orange;
  grid-column: 1/4;  /* Start at line 1, end at line 4 */
}
```

**Understanding Line Numbers:**
```
Line 1        Line 2        Line 3        Line 4
  │             │             │             │
  │   Column 1  │  Column 2   │  Column 3   │
  │             │             │             │
```

When you say `grid-column: 1/4`, you're saying "start at line 1 and end at line 4", which spans all three columns.

### Method 2: Grid Column/Row with Span

```css
.box-2 {
  /* Way 1: Start and end lines */
  /* grid-column-start: 2;
     grid-column-end: 4; */

  /* Way 2: Shorthand with lines */
  /* grid-column: 2 / 4; */

  /* Way 3: Using span (most readable) */
  grid-column: span 2;  /* Spans 2 columns from current position */
}

.box-5 {
  grid-row: 2/4;        /* Spans from row 2 to row 4 */
  grid-column: 3/4;     /* Third column */
}
```

**Span is relative:**
- `grid-column: span 2` means "take up 2 columns wide from wherever I naturally flow"
- `grid-row: span 3` means "take up 3 rows tall"

### Method 3: Template Areas (Recommended for Layouts)

```css
.grid-container {
  display: grid;
  grid-template-columns: 0.5fr 2fr 0.5fr;
  grid-template-rows: 1fr 5fr 1fr;
  grid-template-areas:
    'header header header'
    'left-aside main right-aside'
    'footer footer footer';
}

header { grid-area: header; }
.left-aside { grid-area: left-aside; }
main { grid-area: main; }
.right-aside { grid-area: right-aside; }
footer { grid-area: footer; }
```

This is the most semantic and readable approach for complex layouts.

### Comparison: When to Use Each Method

| Method | Best For | Example Use Case |
|--------|----------|------------------|
| **Line numbers** | Precise positioning | Overlapping elements, specific placements |
| **Span** | Simple spanning items | Feature boxes, images spanning columns |
| **Template areas** | Complete layouts | Page layouts, dashboard grids |

---

## Building Real Layouts

### Pattern 1: Photo Gallery

```html
<h1>My Photo Gallery</h1>
<div class="gallery-container">
  <div class="sandwich-div">
    <img src="https://images.unsplash.com/photo-1553909489-cd47e0907980" alt="Sandwich">
    <p>Sandwich</p>
  </div>
  <div><img src="https://picsum.photos/200/200" alt="Photo"></div>
  <div><img src="https://picsum.photos/200/200" alt="Photo"></div>
  <div><img src="https://picsum.photos/200/200" alt="Photo"></div>
  <div><img src="https://picsum.photos/200/200" alt="Photo"></div>
  <div><img src="https://picsum.photos/200/200" alt="Photo"></div>
  <div><img src="https://picsum.photos/200/200" alt="Photo"></div>
  <div><img src="https://picsum.photos/200/200" alt="Photo"></div>
  <div><img src="https://picsum.photos/200/200" alt="Photo"></div>
</div>
```

```css
.gallery-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  justify-items: center;
  background-color: rgb(255, 213, 213);
  gap: 20px;
  padding: 20px;
}

img {
  box-shadow: rgba(0, 0, 0, 0.851) 0px 3px 8px;
  height: 200px;
  width: 200px;
}

img:hover {
  box-shadow: rgba(7, 255, 3, 0.881) 0px 3px 8px;
}
```

**What's happening here:**
- `repeat(3, 1fr)` creates three equal-width columns
- `justify-items: center` centers each image in its grid cell
- `gap: 20px` adds space between all grid items
- The hover effect changes the shadow color for interactivity

### Pattern 2: Blog Layout with Sidebar

```html
<div class="grid-container">
  <header>
    <h1>Logo</h1>
    <nav>
      <a href="">Home</a>
      <a href="">About me</a>
      <a href="">My projects</a>
      <a href="">Contact me</a>
    </nav>
  </header>
  <aside class="left-aside">Sidebar</aside>
  <main>
    <div class="card">
      <img src="sandwich.jpg" alt="Sandwich">
      <p>Sandwich</p>
    </div>
    <div class="card">
      <img src="sandwich.jpg" alt="Sandwich">
      <p>Sandwich</p>
    </div>
    <!-- More cards -->
  </main>
  <aside class="right-aside">Widgets</aside>
  <footer>Footer</footer>
</div>
```

```css
.grid-container {
  display: grid;
  grid-template-columns: 0.5fr 2fr 0.5fr;
  grid-template-rows: 1fr 5fr 1fr;
  height: 100vh;
  grid-template-areas:
    'header header header'
    'left-aside main right-aside'
    'footer footer footer';
}

header {
  border: 3px solid black;
  grid-area: header;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 50px;
}

nav {
  display: flex;
  justify-content: space-between;
  gap: 30px;
}

.left-aside {
  border: 3px solid red;
  grid-area: left-aside;
  background-color: rgb(255, 220, 220);
}

.right-aside {
  border: 3px solid yellow;
  grid-area: right-aside;
  background-color: rgb(255, 255, 215);
}

main {
  border: 3px solid green;
  grid-area: main;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 40px;
  padding: 40px;
}

img {
  width: 100%;
}

.card {
  box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
}

p {
  text-align: center;
}

footer {
  border: 3px solid orange;
  grid-area: footer;
}

a {
  font-size: 25px;
}
```

**Key Technique: Nested Grid**

Notice that `main` is itself a grid container:
```css
main {
  grid-area: main;        /* This element is in the parent grid */
  display: grid;          /* But it's also a grid container */
  grid-template-columns: repeat(3, 1fr);
  gap: 40px;
  padding: 40px;
}
```

This creates a grid within a grid. The outer grid handles the page layout (header, sidebars, footer), while the inner grid arranges the content cards.

### Pattern 3: Basic Grid with Spanning Items

```html
<main>
  <h1>Basic Grid</h1>
  <div class="grid-container">
    <div class="box">Box 1</div>
    <div class="box box-2">Box 2</div>
    <div class="box">Box 3</div>
    <div class="box">Box 4</div>
    <div class="box box-5">Box 5</div>
    <div class="box">Box 6</div>
    <div class="box">Box 7</div>
    <div class="box">Box 8</div>
  </div>
</main>
```

```css
main {
  border: 5px solid black;
  padding: 20px;
  height: 100vh;
}

.box {
  border: 3px red solid;
  background-color: rgb(255, 206, 206);
}

.grid-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: 100px 400px 50px;
  gap: 20px;
}

.box-2 {
  grid-column: span 2;  /* Spans 2 columns */
}

.box-5 {
  grid-row: 2/4;        /* Spans from row 2 to row 4 */
  grid-column: 3/4;     /* Sits in the third column */
}
```

**Visual Result:**
```
┌─────────┬─────────────────────┬─────────┐
│  Box 1  │      Box 2          │  Box 3  │  (Row 1: 100px)
├─────────┼─────────┬───────────┼─────────┤
│  Box 4  │  Box 6  │  Box 7    │  Box 5  │  (Row 2: 400px)
├─────────┼─────────┴───────────┤         │
│  Box 8  │                     │         │  (Row 3: 50px)
└─────────┴─────────────────────┴─────────┘
```

Box 2 spans 2 columns. Box 5 spans 2 rows and sits in the third column.

---

## Responsive Grid Reconfiguration

One of the most powerful features of grid template areas is how easy it is to completely reconfigure your layout for different screen sizes.

### Desktop to Tablet to Mobile

```css
/* Desktop Layout */
.grid-container {
  display: grid;
  grid-template-columns: 0.5fr 2fr 0.5fr;
  grid-template-rows: 1fr 5fr 1fr;
  height: 100vh;
  grid-template-areas:
    'header header header'
    'left-aside main right-aside'
    'footer footer footer';
}

/* Tablet Layout (800px and below) */
@media (max-width: 800px) {
  .grid-container {
    grid-template-columns: 1.5fr 2fr 1.5fr;
  }
  main {
    grid-template-columns: 1fr 1fr;  /* 2 columns instead of 3 */
  }
}

/* Mobile Layout (400px and below) */
@media (max-width: 400px) {
  .grid-container {
    grid-template-columns: 1fr;
    grid-template-rows: 1fr 1fr 1fr 1fr 1fr;
    grid-template-areas:
      'header'
      'main'
      'left-aside'
      'right-aside'
      'footer';
  }
  main {
    grid-template-columns: 1fr;  /* Single column for mobile */
  }
  .card {
    width: 100%;
  }
}
```

### What Changes at Each Breakpoint

**Desktop (801px+):**
```
┌─────────────────────────────────┐
│           HEADER                │
├──────────┬──────────────┬───────┤
│  LEFT    │              │ RIGHT │
│  ASIDE   │     MAIN     │ ASIDE │
│          │  (3 columns) │       │
├──────────┴──────────────┴───────┤
│           FOOTER                │
└─────────────────────────────────┘
```

**Tablet (400px to 800px):**
```
┌────────────────────────────┐
│         HEADER             │
├───────┬────────────┬───────┤
│ LEFT  │            │ RIGHT │
│ ASIDE │    MAIN    │ ASIDE │
│       │ (2 columns)│       │
├───────┴────────────┴───────┤
│         FOOTER             │
└────────────────────────────┘
```

**Mobile (below 400px):**
```
┌───────────────┐
│    HEADER     │
├───────────────┤
│               │
│     MAIN      │
│  (1 column)   │
│               │
├───────────────┤
│  LEFT ASIDE   │
├───────────────┤
│  RIGHT ASIDE  │
├───────────────┤
│    FOOTER     │
└───────────────┘
```

Notice how the grid template areas completely changes the layout order and structure. On mobile, the main content comes first, then the sidebars stack below it.

### Best Practices for Responsive Grids

1. **Mobile First or Desktop First?**
   - Mobile first: Start with single column, add complexity for larger screens
   - Desktop first (shown above): Start complex, simplify for smaller screens
   - Choose based on your content priorities

2. **Common Breakpoints:**
   ```css
   /* Mobile: 0-600px */
   /* Tablet: 601px-900px */
   /* Desktop: 901px+ */
   ```

3. **Use fr Units for Flexibility:**
   ```css
   /* BAD: Fixed widths don't adapt */
   grid-template-columns: 200px 800px 200px;

   /* GOOD: Fractional units adapt to container */
   grid-template-columns: 1fr 4fr 1fr;
   ```

4. **Adjust Gap for Screen Size:**
   ```css
   .grid-container {
     gap: 40px;  /* Desktop */
   }

   @media (max-width: 800px) {
     .grid-container {
       gap: 20px;  /* Tablet */
     }
   }

   @media (max-width: 400px) {
     .grid-container {
       gap: 10px;  /* Mobile */
     }
   }
   ```

---

## Gallery Pattern

The gallery pattern is one of the most common uses for CSS Grid. Here's a production-ready implementation.

### Responsive Gallery with Auto-Fill

```css
.gallery-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 20px;
  padding: 20px;
}
```

**What's happening:**
- `repeat(auto-fill, ...)` creates as many columns as will fit
- `minmax(200px, 1fr)` makes each column at least 200px, but allows growth
- This automatically adapts to any screen size without media queries

### Gallery with Featured Items

```css
.gallery-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 20px;
}

.gallery-item {
  height: 200px;
  overflow: hidden;
}

.gallery-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.featured {
  grid-column: span 2;  /* Featured items span 2 columns */
  grid-row: span 2;     /* And 2 rows */
}
```

**Usage:**
```html
<div class="gallery-container">
  <div class="gallery-item featured">
    <img src="featured.jpg" alt="Featured">
  </div>
  <div class="gallery-item">
    <img src="photo1.jpg" alt="Photo">
  </div>
  <div class="gallery-item">
    <img src="photo2.jpg" alt="Photo">
  </div>
  <!-- More items -->
</div>
```

### Pinterest-Style Masonry Grid

For a Pinterest-style layout where items have different heights:

```css
.masonry-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  grid-auto-rows: 10px;  /* Small row height for fine control */
  gap: 20px;
}

.masonry-item {
  /* JavaScript calculates how many rows each item needs */
  /* Example: grid-row-end: span 30 for a tall item */
}
```

Note: True masonry layout requires JavaScript to calculate row spans based on content height, or use the upcoming `grid-template-rows: masonry` property (limited browser support as of 2025).

---

## Advanced Techniques

### Technique 1: Overlapping Grid Items

```css
.grid-container {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: repeat(4, 100px);
}

.background-image {
  grid-column: 1 / 4;
  grid-row: 1 / 4;
  z-index: 1;
}

.text-overlay {
  grid-column: 2 / 5;
  grid-row: 2 / 5;
  z-index: 2;
  background: rgba(255, 255, 255, 0.9);
  padding: 20px;
}
```

Both items occupy overlapping grid cells, creating a layered effect. Use z-index to control which is on top.

### Technique 2: Empty Grid Cells

Use a dot (.) to create empty grid cells:

```css
.grid-container {
  grid-template-areas:
    'header header header'
    'sidebar main .'
    'footer footer footer';
}
```

The dot in the top-right creates an intentionally empty space.

### Technique 3: Asymmetric Grids

```css
.grid-container {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr;
  grid-template-rows: 100px 1fr 1fr 50px;
}
```

This creates columns where the first is twice as wide as the others, and rows with varying heights.

### Technique 4: Grid with Flexbox Items

```css
.grid-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}

.grid-item {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
```

Each grid item is also a flex container, giving you fine control over content inside each grid cell.

---

## Common Patterns

### Pattern 1: Dashboard Layout

```css
.dashboard {
  display: grid;
  grid-template-columns: 250px 1fr;
  grid-template-rows: 60px 1fr 40px;
  height: 100vh;
  grid-template-areas:
    'sidebar header'
    'sidebar main'
    'sidebar footer';
}

.sidebar { grid-area: sidebar; }
.header { grid-area: header; }
.main { grid-area: main; }
.footer { grid-area: footer; }
```

### Pattern 2: Holy Grail Layout

```css
.holy-grail {
  display: grid;
  grid-template-columns: 200px 1fr 200px;
  grid-template-rows: auto 1fr auto;
  min-height: 100vh;
  grid-template-areas:
    'header header header'
    'left-sidebar content right-sidebar'
    'footer footer footer';
}
```

### Pattern 3: Card Grid

```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 30px;
  padding: 20px;
}

.card {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
```

---

## Summary

**Key Takeaways:**
1. **Grid template areas** provide visual, semantic layout definitions
2. **Three placement methods** - line numbers, span, or template areas
3. **Nested grids** let you create grids within grids for complex layouts
4. **Responsive reconfiguration** is easy with media queries changing grid-template-areas
5. **Gallery patterns** use auto-fill for responsive image grids
6. **Fr units** create flexible, proportional columns and rows

**Best Practice Pattern:**

```css
.page-layout {
  display: grid;
  grid-template-columns: 1fr 3fr 1fr;
  grid-template-rows: auto 1fr auto;
  min-height: 100vh;
  gap: 20px;
  grid-template-areas:
    'header header header'
    'left main right'
    'footer footer footer';
}

@media (max-width: 768px) {
  .page-layout {
    grid-template-columns: 1fr;
    grid-template-areas:
      'header'
      'main'
      'left'
      'right'
      'footer';
  }
}
```

---

## See Also

- [CSS Flexbox Complete Guide](./CSS_Flexbox_Complete_Guide.md) - Flexbox for one-dimensional layouts
- [CSS Cheat Sheet](../cheatsheets/CSS_Cheat_Sheet.md) - Quick CSS reference with positioning and alignment
- [CSS Layout Guide](./CSS_Layout_Guide.md) - Comprehensive layout techniques
- [Bootstrap Cheat Sheet](../cheatsheets/Bootstrap_Cheat_Sheet.md) - Bootstrap grid system
- [React Basics Guide](./React_Basics_Guide.md) - Component layouts with Grid
- [Portfolio Web Development Guide](./Portfolio_Web_Development_Guide.md) - Practical layout examples

---

